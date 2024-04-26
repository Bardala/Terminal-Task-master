from controllers.base_controller import BaseController
from utils.error_handler import *
from utils.helpers import (
    MAIN_COMMAND_COLOR,
    MOOD_COMMAND_COLOR,
    PROJECT_COMMAND_COLOR,
    SETTINGS_COMMAND_COLOR,
    TODO_COMMAND_COLOR,
    Goodbye,
)
from database.sql_data_store import SqlDataStore
from colorama import init
from controllers.todos import Todos
from controllers.vsCodeProjectOpener import VSCodeProjectOpener
from controllers.mood_manager import MyModeManager
from controllers.windows_settings import WindowsSettings


class Main(BaseController):
    def __init__(self, cmd_name: str, db: SqlDataStore, cmd_color: str):
        super().__init__(cmd_name, db, cmd_color)
        self.todos = Todos("todo> ", self.db, TODO_COMMAND_COLOR)
        self.mood = MyModeManager("mood> ", self.db, MOOD_COMMAND_COLOR)
        self.vsCodeProjectOpener = VSCodeProjectOpener("project> ", self.db, PROJECT_COMMAND_COLOR)
        self.windows_settings = WindowsSettings("settings> ", self.db, SETTINGS_COMMAND_COLOR)
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
    main = Main("bardala> ", db, MAIN_COMMAND_COLOR)
    main.run()
    Goodbye()
    db.close()
