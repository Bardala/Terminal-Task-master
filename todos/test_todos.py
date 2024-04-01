import unittest

from todos import Todos


class TodosTestCase(unittest.TestCase):
    def setUp(self):
        self.todos = Todos()

    def test_add(self):
        self.todos.add("Task 1")
        self.assertEqual(len(self.todos.todos), 1)
        self.assertEqual(self.todos.todos[0], "Task 1")

    def test_delete(self):
        self.todos.add("Task 1")
        self.todos.add("Task 2")
        self.todos.delete("Task 1")
        self.assertEqual(len(self.todos.todos), 1)
        self.assertEqual(self.todos.todos[0], "Task 2")

    def test_update_existing_todo(self):
        self.todos.add("Task 1")
        self.todos.update(1, "Updated Task 1")
        self.assertEqual(len(self.todos.todos), 1)
        self.assertEqual(self.todos.todos[0], "Updated Task 1")

    def test_update_non_existing_todo(self):
        self.todos.add("Task 1")
        self.todos.update(2, "Updated Task 2")
        self.assertEqual(len(self.todos.todos), 1)
        self.assertEqual(self.todos.todos[0], "Task 1")

    def test_run_todo_mode_add(self):
        # TODO: Implement this test case
        pass

    def test_run_todo_mode_exit(self):
        # TODO: Implement this test case
        pass

    def test_run_todo_mode_invalid_command(self):
        # TODO: Implement this test case
        pass


if __name__ == "__main__":
    unittest.main()
