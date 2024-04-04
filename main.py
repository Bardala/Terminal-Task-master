from todos import Todos
from utils.helpers import catch_errors_in_class, colored_input
from database.sql_data_store import SqlDataStore
from colorama import Fore, Back, Style, init
from vsCodeProjectOpener import VSCodeProjectOpener


@catch_errors_in_class
class main:
    def __init__(self):
        self.db = SqlDataStore()
        self.todos = Todos(self.db)
        self.vsCodeProjectOpener = VSCodeProjectOpener(self.db)

    def run(self):
        bardala = colored_input("bardala> ")

        if bardala == "todo":
            self.todos.run_todo_mode()
        elif bardala == "project":
            self.vsCodeProjectOpener.run_project_mode()
        elif bardala == "/":
            print(Fore.LIGHTBLACK_EX + "Goodbye")
            self.db.close()
            return
        else:
            print(Fore.RED + "Invalid command")
        self.run()


if __name__ == "__main__":
    init(autoreset=True)
    main = main()
    main.run()
