from todo import Todo

class Todos:
  def __init__(self):
    self.todos = []

  def add(self, todo):
    self.todos.append(todo)

  def delete(self, todo):
    self.todos.remove(todo)

  def update(self, todo_id, new_task):
    for todo in self.todos:
      if todo_id == todo.id:
        new_todo = Todo(id, new_task, todo.status)
        todo_index = todo.id - 1
        self.todos[todo_index] = new_todo
        return self.todos
    print("This todo_id doesn't exit")

  def run_todo_mode(self):
    command = input("todo> ")
    if command == "add":
      print("add new todo")
      while True:
        input_task = input(">>> ")
        if input_task == "exit" and len(self.todos) != 0: 
          print("id | task | status | createdAt")
          for todo in self.todos:
            print(f"{todo.id} | {todo.task} | {todo.status} | {todo.createdAt}")
          break
        id = 1 if len(self.todos) == 0 else len(self.todos) + 1
        new_todo = Todo(id, input_task, "incomplete")
        self.add(new_todo)
      self.run_todo_mode()
    elif command == "exit":
      print("get out of todo mode")
      return
    else:
      print("Invalid command")
      self.run_todo_mode()