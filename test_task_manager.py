import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        result = self.manager.add_task("Task 1")
        self.assertTrue(result)
        self.assertEqual(len(self.manager.tasks), 1)

    def test_delete_task(self):
        self.manager.add_task("Task 1")
        result = self.manager.delete_task(0)
        self.assertTrue(result)

    def test_edit_task(self):
        self.manager.add_task("Old")
        result = self.manager.edit_task(0, "New")
        self.assertTrue(result)
        self.assertEqual(self.manager.tasks[0], "New")

    def test_file_integration(self):
        self.manager.add_task("Test")
        self.manager.save_to_file("test.txt")

        new_manager = TaskManager()
        new_manager.load_from_file("test.txt")

        self.assertEqual(len(new_manager.tasks), 1)

if __name__ == "__main__":
    unittest.main()