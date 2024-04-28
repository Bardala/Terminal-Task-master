from controllers.base_controller import BaseController
from utils.error_handler import *
from utils.helpers import COLOR, Goodbye
from database.sql_data_store import SqlDataStore
from colorama import init
from controllers.todos import Todos
from controllers.vsCodeProjectOpener import VSCodeProjectOpener
from controllers.mood_manager import MyModeManager
from controllers.windows_settings import WindowsSettings


class Main(BaseController):
    def __init__(self, cmd_name: str, db: SqlDataStore, cmd_color: str):
        super().__init__(cmd_name, db, cmd_color)
        self.todos = Todos("todo> ", self.db, COLOR.TODO_COMMAND.value)
        self.mood = MyModeManager("mood> ", self.db, COLOR.MOOD_COMMAND.value)
        self.vsCodeProjectOpener = VSCodeProjectOpener(
            "project> ", self.db, COLOR.PROJECT_COMMAND.value
        )
        self.windows_settings = WindowsSettings("settings> ", self.db, COLOR.SETTINGS_COMMAND.value)
        self.command_dict: dict[str, callable] = {
            "todo": self.todos.run,
            "project": self.vsCodeProjectOpener.run,
            "mood": self.mood.run,
            "settings": self.windows_settings.run,
            "clear": self.clear_screen,
            "help": self.help,
        }


if __name__ == "__main__":
    init(autoreset=True)
    db = SqlDataStore()
    main = Main("bardala> ", db, COLOR.MAIN_COMMAND.value)
    main.run()
    Goodbye()
    db.close()
