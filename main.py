from controllers.base_controller import BaseController
from utils.error_handler import *
from utils.helpers import Goodbye, class_runner, helper
from database.sql_data_store import SqlDataStore
from colorama import Fore, init
from controllers.todos import Todos
from controllers.vsCodeProjectOpener import VSCodeProjectOpener
from controllers.mood_manager import MyModeManager
from controllers.windows_settings import WindowsSettings


@catch_errors_in_class
class main(BaseController):
    def __init__(self, cmd_name: str, db: SqlDataStore):
        super().__init__(cmd_name, db)
        self.todos = Todos(self.db, "todo> ")
        self.mood = MyModeManager(self.db, "mood> ")
        self.vsCodeProjectOpener = VSCodeProjectOpener(self.db, "project> ")
        self.windows_settings = WindowsSettings("settings> ", self.db)
        self.command_dict: dict[str, callable] = {
            "todo": self.todos.run,
            "project": self.vsCodeProjectOpener.run,
            "mood": self.mood.run,
            "settings": self.windows_settings.run,
            "clear": self.clear_screen,
            "help": self.help,
        }

    def clear_screen(self) -> None:
        super().clear_screen()

    def help(self) -> None:
        helper(self.command_dict)

    @catch_errors
    def run(self) -> None:
        class_runner(self.cmd_name, self.command_dict, Fore.GREEN, self.db)


if __name__ == "__main__":
    init(autoreset=True)
    db = SqlDataStore()
    main = main("bardala> ", db)
    main.run()
    Goodbye()
    db.close()
