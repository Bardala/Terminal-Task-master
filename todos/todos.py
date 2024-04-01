from todo.todo import Todo
from utils.helpers import command as cmd


class Todos:
    def __init__(self):
        self.todos = []

    def add(self):
        print("add new todo")
        while True:
            input_task = input(">>> ")
            if input_task == "/":
                if len(self.todos) == 0:
                    print("You have no todos to add")
                    break
                self.show_todos()
                break
            id = len(self.todos) + 1
            new_todo = Todo(id, input_task, "incomplete")
            self.todos.append(new_todo)

    def delete(self, todo):
        self.todos.remove(todo)

    def update(self, todo_id, new_task):
        for todo in self.todos:
            if todo_id == todo.id:
                new_todo = Todo(id, new_task, todo.status)
                todo_index = todo.id - 1
                self.todos[todo_index] = new_todo
                return self.todos
        print("This todo_id doesn't exist")

    def toggle(self):
        self.show_todos()
        id = int(cmd(input("todo_id> ")))
        for todo in self.todos:
            if id == todo.id:
                if todo.status == "incomplete":
                    todo.status = "complete"
                else:
                    todo.status = "incomplete"
                print(f"{todo.id}. {todo.task} is now {todo.status}")

    def show_todos(self):
        for todo in self.todos:
            print(f"{todo.id}. {todo.task} - {todo.status}")

    def run_todo_mode(self):
        command = cmd(input("todo> "))

        if command == "add":
            self.add()
        elif command == "toggle":
            self.toggle()
        elif command == "show":
            self.show_todos()
        elif command == "":
            pass
        elif command == "/":
            print("\nGet out of todo mode")
            return
        else:
            print("Invalid command, try entering 'add', 'toggle', 'show' or '/'")
        self.run_todo_mode()
