from datetime import datetime
from typing import Any, List, Dict, Literal, Union
from colorama import Fore
from .base_controller import BaseController
from database.sql_data_store import SqlDataStore
from utils.error_handler import *
from utils.helpers import *


# todo: add a method to delete more than one todo, not all
@catch_errors_in_class
class Todos(BaseController):
    def __init__(self, db: SqlDataStore, cmd_name: str = "todo> "):
        super().__init__(cmd_name, db)
        self.command_dict = {
            "add": self.add,
            "toggle": self.toggle,
            "done": self.set_done,
            "list": self.show_todos,
            "delete": self.delete,
            "update": self.update,
            "delete_all": self.delete_all,
            "clear": self.clear_screen,
            "help": self.help,
        }

    def add(self) -> None:
        print("add new todo")
        while True:
            input_task = colored_input(">>> ", Fore.CYAN)
            if check_user_input(input_task):
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

    def delete(self, id: int = None) -> None:  # todo
        todo_id = id or self._todo_id()
        if check_user_input(todo_id):
            return
        todo = self.db.get_todo_by_id(todo_id)
        if todo:
            self.check_is_package(todo, "delete")
            self.db.delete_todo_by_id(todo_id)
            print(f"'{todo['task']}' has been deleted")
            return
        print("This todo_id doesn't exist")

    def update(self) -> None:
        todo_id = self._todo_id()
        if check_user_input(todo_id):
            return
        new_task = command(input("new task> "))
        todo = self.db.get_todo_by_id(todo_id)
        if not todo:
            self.db.update_todo_by_id(todo_id, new_task)
            print(f"'{todo['task']}' has been updated to '{new_task}'")
            return
        print("This todo_id doesn't exist")

    def toggle(self, id: int = None) -> None:
        todo_id = id or self._todo_id()
        if check_user_input(todo_id):
            return
        todo = self.db.get_todo_by_id(todo_id)
        if todo:
            self.check_is_package(todo, "toggle")
            self.db.toggle_todo(todo_id)
            status = "completed" if not todo["status"] else "incomplete"
            print(f"'{todo['task']}' is now {status}")
            return
        print("This todo_id doesn't exist")

    def set_done(self, id: int = None) -> None:
        todo_id = id or self._todo_id()
        if check_user_input(todo_id):
            return
        todo = self.db.get_todo_by_id(todo_id)
        if todo:
            if todo["status"] == 1:
                print("This todo is already completed")
            else:
                self.check_is_package(todo, "done")
                self.db.set_done(todo_id)
                print(f"'{todo['task']}' is now completed")
        else:
            print("This todo_id doesn't exist")

    def check_is_package(self, todo, operation: Literal["toggle", "done", "delete"]) -> None:
        if todo["task"].startswith("__"):
            todo_package = self.todo_package(todo["id"])
            for todo in todo_package["todos"]:
                self.command_dict[operation](todo["id"])

    def todo_package(self, todo_id: int) -> Dict[str, Any]:
        todos = self.todos()
        package = {"head_todo_id": None, "todos": []}
        package["head_todo_id"] = todo_id
        for todo in todos:
            if todo["id"] > todo_id:
                if todo["task"].startswith("__"):
                    break
                package["todos"].append(todo)
        return package

    def _todo_id(self) -> int:
        """Helper function to get todo_id from user input"""
        return int(colored_input("todo_id> ", TODO_ID_COLOR))

    def show_todos(self) -> None:
        if len(self.todos()) == 0:
            print("You have no todos")
            return
        for todo in self.todos():
            print(f"{todo['id']}. {todo['task']} - {todo['status']}")

    def delete_all(self) -> None:
        if len(self.todos()) == 0:
            print("You have no todos to delete")
            return
        submit = input("Are you sure you want to delete all todos? (y/n) ")
        if submit.lower() != "y":
            return
        self.db.delete_all_todos()
        print("All todos have been deleted")

    def todos(self) -> List[Dict[str, Union[int, str]]]:
        """Get all todos from the database"""
        return self.db.get_all_todos()

    def help(self) -> None:
        helper(self.command_dict)

    def clear_screen(self) -> None:
        super().clear_screen()

    def run(self) -> None:
        class_runner(self.cmd_name, self.command_dict, TODO_COMMAND_COLOR)
