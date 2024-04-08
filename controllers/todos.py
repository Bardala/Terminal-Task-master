from datetime import datetime

from colorama import Fore
from utils.helpers import (
    TODO_COMMAND_COLOR,
    TODO_ID_COLOR,
    class_runner,
    colored_input,
    command as cmd,
    helper,
)


class Todos:
    def __init__(self, db):
        self.db = db
        self.cmd_name = "todo> "
        self.command_dict = {
            "add": self.add,
            "toggle": self.toggle,
            "show": self.show_todos,
            "list": self.show_todos,
            "ls": self.show_todos,
            "delete": self.delete,
            "update": self.update,
            "delete_all": self.delete_all,
            "help": self.help,
        }

    def add(self):
        print("add new todo")
        while True:
            input_task = colored_input(">>> ", Fore.CYAN)
            if input_task == "/":
                if len(self.todos()) == 0:
                    print("You have no todos to add")
                    return
                self.show_todos()
                return
            id = self.db.get_last_todo_id() + 1
            new_todo = {
                "id": id,
                "task": input_task,
                "status": 0,
                "due_date": None,
                "created_at": datetime.now(),
            }
            self.db.add_todo(new_todo)

    def delete(self):
        todo_id = self._todo_id()
        todo = self.db.get_todo_by_id(todo_id)
        if todo:
            self.db.delete_todo_by_id(todo_id)
            print(f"'{todo['task']}' has been deleted")
            return
        print("This todo_id doesn't exist")

    def update(self):
        todo_id = self._todo_id()
        new_task = cmd(input("new task> "))
        todo = self.db.get_todo_by_id(todo_id)
        if not todo:
            self.db.update_todo_by_id(todo_id, new_task)
            print(f"'{todo['task']}' has been updated to '{new_task}'")
            return
        print("This todo_id doesn't exist")

    def toggle(self):
        todo_id = self._todo_id()
        todo = self.db.get_todo_by_id(todo_id)
        if todo:
            self.db.toggle_todo(todo_id)
            status = "completed" if not todo["status"] else "incomplete"
            print(f"'{todo['task']}' is now {status}")
            return
        print("This todo_id doesn't exist")

    def _todo_id(self):
        return int(
            colored_input(
                "todo_id> ",
                TODO_ID_COLOR,
            )
        )

    def show_todos(self):
        if len(self.todos()) == 0:
            print("You have no todos")
            return
        for todo in self.todos():
            print(f"{todo['id']}. {todo['task']} - {todo['status']}")

    def delete_all(self):
        if len(self.todos()) == 0:
            print("You have no todos to delete")
            return
        self.db.delete_all_todos()
        print("All todos have been deleted")

    def todos(self):
        return self.db.get_all_todos()

    def help(self):
        helper(self.command_dict)

    def run_todo_mode(self):
        class_runner(self.cmd_name, self.command_dict, TODO_COMMAND_COLOR)
