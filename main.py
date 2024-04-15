from utils.error_handler import *
from utils.helpers import class_runner, helper
from database.sql_data_store import SqlDataStore
from colorama import Fore, init
from database.sql_data_store import SqlDataStore
from controllers.todos import Todos
from controllers.vsCodeProjectOpener import VSCodeProjectOpener
from controllers.mood_manager import MyModeManager


@catch_errors_in_class
class main:
    def __init__(self):
        self.cmd_name = "bardala> "
        self.db = SqlDataStore()
        self.todos = Todos(self.db)
        self.mood = MyModeManager(self.db)
        self.vsCodeProjectOpener = VSCodeProjectOpener(self.db)
        self.command_dict = {
            "todo": self.todos.run_todo_mode,
            "project": self.vsCodeProjectOpener.run_project_mode,
            "mood": self.mood.run_mood_mode,
            "help": self.help,
        }

    def help(self):
        helper(self.command_dict)

    def run(self):
        class_runner(self.cmd_name, self.command_dict, Fore.GREEN, self.db)


if __name__ == "__main__":
    init(autoreset=True)
    main = main()
    main.run()
