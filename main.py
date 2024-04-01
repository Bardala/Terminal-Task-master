from todos.todos import Todos
from utils.helpers import command as cmd


class main:
    def __init__(self):
        self.todos = Todos()

    def run(self):
        mode = cmd(input("\nbardala> "))

        if mode == "todo":
            self.todos.run_todo_mode()
        elif mode == "/":
            print("\nGoodbye")
            return
        else:
            print("Invalid command")
        self.run()


if __name__ == "__main__":
    main = main()
    main.run()
