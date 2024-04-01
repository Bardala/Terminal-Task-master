from todos.todos import Todos
from utils.helpers import command as cmd
from database.sql_data_store import SqlDataStore


class main:
    def __init__(self):
        self.db = SqlDataStore()
        self.todos = Todos(self.db)

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
