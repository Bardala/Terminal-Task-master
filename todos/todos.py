from datetime import datetime
from utils.helpers import command as cmd


class Todos:
    def __init__(self, db):
        self.db = db

    def add(self):
        print("add new todo")
        while True:
            input_task = input(">>> ")
            if input_task == "/":
                if len(self.todos()) == 0:
                    print("You have no todos to add")
                    return
                self.show_todos()
                return
            id = len(self.todos()) + 1  # todo: get the last id from the db
            new_todo = {
                "id": id,
                "task": input_task,
                "status": 0,
                "due_date": None,
                "created_at": datetime.now(),
            }
            self.db.add_todo(new_todo)

    # todo: connect these methods to the db
    def delete(self):
        todo_id = int(cmd(input("todo_id> ")))
        todo = self.db.get_todo_by_id(todo_id)
        if todo:
            self.db.delete_todo_by_id(todo_id)
            print(f"'{todo['task']}' has been deleted")
            return
        print("This todo_id doesn't exist")

    def update(self):
        todo_id = int(cmd(input("todo_id> ")))
        new_task = cmd(input("new task> "))
        todo = self.db.get_todo_by_id(todo_id)
        if not todo:
            self.db.update_todo_by_id(todo_id, new_task)
            print(f"'{todo['task']}' has been updated to '{new_task}'")
            return
        print("This todo_id doesn't exist")

    def toggle(self):  #! This method is not working properly
        id = int(cmd(input("todo_id> ")))
        for todo in self.todos():
            if id == todo["id"]:
                self.db.toggle_todo(id)
                status = "completed" if not todo["status"] else "incomplete"
                print(f"{todo['id']}. '{todo['task']}' is now {status}")

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
        print("Enter 'add' to add a new todo")
        print("Enter 'toggle' to toggle a todo")
        print("Enter 'show' to show all todos")
        print("Enter 'delete' to delete a todo")
        print("Enter 'update' to update a todo")
        print("Enter delete_all to delete all todos")
        print("Enter '/' to exit todo mode")

    def run_todo_mode(self):
        command = cmd(input("todo> "))

        if command == "add":
            self.add()
        elif command == "toggle":
            self.toggle()
        elif command == "show":
            self.show_todos()
        elif command == "delete":
            self.delete()
        elif command == "update":
            self.update()
        elif command == "delete_all":
            self.delete_all()

        elif command == "help":
            self.help()
        elif command == "":
            pass
        elif command == "/":
            print("\nGet out of todo mode")
            return
        else:
            print("Invalid command, try entering 'add', 'toggle', 'show' or '/'")
        self.run_todo_mode()
