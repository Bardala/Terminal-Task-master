from todo import Todo
from todos import Todos

class main:
  def __init__(self):
    self.todos = Todos()

  def run(self):
    mode = input("bardala> ")

    if mode == 'todo':
      self.todos.run_todo_mode()
    elif mode == 'exit':
      print("Goodbye")
      return
    else:
      self.run()

if __name__ == "__main__":
  main = main()
  main.run()