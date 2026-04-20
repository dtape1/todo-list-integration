"""
Модуль для керування списком задач.
Надає клас TaskManager для додавання, редагування,
видалення, збереження та завантаження задач.
"""
 
 
class TaskManager:
    """
    Клас для управління списком задач.
 
    Атрибути:
        tasks (list): Список рядків — поточні задачі.
    """
 
    def __init__(self):
        """Ініціалізує TaskManager з порожнім списком задач."""
        self.tasks = []
 
    def add_task(self, task: str) -> bool:
        """
        Додає нову задачу до списку.
 
        Args:
            task (str): Текст задачі.
 
        Returns:
            bool: True якщо задачу додано, False якщо текст порожній.
        """
        task = task.strip()
        if task:
            self.tasks.append(task)
            return True
        return False
 
    def delete_task(self, index: int) -> bool:
        """
        Видаляє задачу за індексом.
 
        Args:
            index (int): Індекс задачі у списку.
 
        Returns:
            bool: True якщо видалено успішно, False якщо індекс хибний.
        """
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False
 
    def edit_task(self, index: int, new_text: str) -> bool:
        """
        Редагує задачу за індексом.
 
        Args:
            index (int): Індекс задачі у списку.
            new_text (str): Новий текст задачі.
 
        Returns:
            bool: True якщо редагування успішне, False інакше.
        """
        new_text = new_text.strip()
        if new_text and 0 <= index < len(self.tasks):
            self.tasks[index] = new_text
            return True
        return False
 
    def load_from_file(self, filepath: str) -> None:
        """
        Завантажує задачі з текстового файлу.
        Кожен непорожній рядок стає окремою задачею.
 
        Args:
            filepath (str): Шлях до файлу.
        """
        with open(filepath, "r", encoding="utf-8") as f:
            # Використовуємо генератор для економії пам'яті
            self.tasks = [line.strip() for line in f if line.strip()]
 
    def save_to_file(self, filepath: str) -> None:
        """
        Зберігає задачі у текстовий файл.
 
        Args:
            filepath (str): Шлях до файлу.
        """
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(self.tasks) + "\n" if self.tasks else "")
 
    def get_task_count(self) -> int:
        """
        Повертає кількість задач.
 
        Returns:
            int: Кількість задач у списку.
        """
        return len(self.tasks)