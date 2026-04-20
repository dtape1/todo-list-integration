"""
Головний модуль графічного інтерфейсу To-Do List застосунку.
Використовує tkinter для GUI та TaskManager для керування задачами.
"""

import tkinter as tk
from tkinter import messagebox, filedialog
from task_manager_optimized import TaskManager
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    encoding="utf-8"
)

manager = TaskManager()


def update_listbox():
    """Оновлює відображення списку задач у listbox."""
    listbox.delete(0, tk.END)
    for i, task in enumerate(manager.tasks, 1):
        listbox.insert(tk.END, f"{i}. {task}")


def select_task(event):
    """
    Обробник події вибору задачі у listbox.
    Заповнює поле введення обраною задачею.
    """
    try:
        selected = listbox.curselection()[0]
        entry.delete(0, tk.END)
        entry.insert(0, manager.tasks[selected])
    except IndexError:
        pass


def open_file():
    """Відкриває діалог вибору файлу та завантажує задачі з нього."""
    filepath = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt")]
    )
    if filepath:
        manager.load_from_file(filepath)
        logging.info("Файл відкрито")
        update_listbox()


def save_file():
    """Відкриває діалог збереження та зберігає задачі у файл."""
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if filepath:
        manager.save_to_file(filepath)
        logging.info("Файл збережено")
        messagebox.showinfo("Успіх", "Файл збережено")


def add_task():
    """Зчитує текст з поля введення та додає нову задачу."""
    task = entry.get()
    if manager.add_task(task):
        logging.info("Додано задачу")
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Помилка", "Введіть завдання")


def delete_task():
    """Видаляє обрану задачу зі списку."""
    try:
        selected = listbox.curselection()[0]
        if manager.delete_task(selected):
            logging.info("Видалено задачу")
            update_listbox()
    except IndexError:
        messagebox.showwarning("Помилка", "Оберіть завдання")


def edit_task():
    """Замінює текст обраної задачі на новий із поля введення."""
    try:
        selected = listbox.curselection()[0]
        new_text = entry.get()

        if manager.edit_task(selected, new_text):
            logging.info("Відредаговано задачу")
            entry.delete(0, tk.END)
            update_listbox()
        else:
            messagebox.showwarning("Помилка", "Введіть новий текст")
    except IndexError:
        messagebox.showwarning("Помилка", "Оберіть завдання")


# --- Побудова вікна ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Додати", width=20, command=add_task).pack(pady=5)
tk.Button(root, text="Видалити", width=20, command=delete_task).pack(pady=5)
tk.Button(root, text="Редагувати", width=20, command=edit_task).pack(pady=5)

tk.Button(root, text="Відкрити файл", width=20, command=open_file).pack(pady=5)
tk.Button(root, text="Зберегти як", width=20, command=save_file).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=12)
listbox.pack(pady=10)

listbox.bind("<<ListboxSelect>>", select_task)

root.mainloop()