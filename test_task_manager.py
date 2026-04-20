"""
Тести для TaskManager (оптимізована версія).
Перевіряє всі основні операції: додавання, видалення,
редагування задач, збереження та завантаження файлу.
"""

import unittest
import os
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    """Тести для класу TaskManager."""

    def setUp(self):
        """Ініціалізує новий TaskManager перед кожним тестом."""
        self.manager = TaskManager()

    def test_add_task(self):
        """Перевірка додавання задачі."""
        result = self.manager.add_task("Task 1")
        self.assertTrue(result)
        self.assertEqual(len(self.manager.tasks), 1)

    def test_add_empty_task(self):
        """Порожній рядок не повинен додаватись."""
        result = self.manager.add_task("   ")
        self.assertFalse(result)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_delete_task(self):
        """Перевірка видалення задачі."""
        self.manager.add_task("Task 1")
        result = self.manager.delete_task(0)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_delete_invalid_index(self):
        """Видалення за хибним індексом повертає False."""
        result = self.manager.delete_task(99)
        self.assertFalse(result)

    def test_edit_task(self):
        """Перевірка редагування задачі."""
        self.manager.add_task("Old")
        result = self.manager.edit_task(0, "New")
        self.assertTrue(result)
        self.assertEqual(self.manager.tasks[0], "New")

    def test_edit_invalid_index(self):
        """Редагування за хибним індексом повертає False."""
        result = self.manager.edit_task(99, "Text")
        self.assertFalse(result)

    def test_get_task_count(self):
        """Перевірка підрахунку задач."""
        self.assertEqual(self.manager.get_task_count(), 0)
        self.manager.add_task("Task 1")
        self.assertEqual(self.manager.get_task_count(), 1)

    def test_file_integration(self):
        """Перевірка збереження та завантаження з файлу."""
        self.manager.add_task("Test")
        self.manager.save_to_file("test_temp.txt")

        new_manager = TaskManager()
        new_manager.load_from_file("test_temp.txt")

        self.assertEqual(len(new_manager.tasks), 1)
        self.assertEqual(new_manager.tasks[0], "Test")

        # Очищення тимчасового файлу
        if os.path.exists("test_temp.txt"):
            os.remove("test_temp.txt")


if __name__ == "__main__":
    unittest.main()