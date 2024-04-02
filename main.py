from todos.todos import Todos
from utils.helpers import command as cmd, stdin
from database.sql_data_store import SqlDataStore
from colorama import Fore, Back, Style, init


class main:
    def __init__(self):
        self.db = SqlDataStore()
        self.todos = Todos(self.db)

    def run(self):
        bardala = stdin()

        if bardala == "todo":
            self.todos.run_todo_mode()
        elif bardala == "/":
            print(Fore.BLACK + "Goodbye")
            self.db.close()
            return
        else:
            print(Fore.RED + "Invalid command")
        self.run()


if __name__ == "__main__":
    init(autoreset=True)
    main = main()
    main.run()
