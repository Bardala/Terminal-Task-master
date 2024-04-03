import unittest
from datetime import datetime

from todo import Todo


class TodoTests(unittest.TestCase):
    def setUp(self):
        self.todo = Todo(1, "Buy groceries", "Incomplete")

    def test_update_task(self):
        new_task = "Clean the house"
        updated_task = self.todo.update_task(new_task)
        self.assertEqual(updated_task, new_task)
        self.assertEqual(self.todo.task, new_task)

    def test_update_status(self):
        new_status = "Complete"
        updated_status = self.todo.update_status(new_status)
        self.assertEqual(updated_status, new_status)
        self.assertEqual(self.todo.status, new_status)

    def test_createdAt(self):
        self.assertIsInstance(self.todo.createdAt, datetime)


if __name__ == "__main__":
    unittest.main()
