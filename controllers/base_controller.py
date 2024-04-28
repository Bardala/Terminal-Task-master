from database.sql_data_store import SqlDataStore
from utils.error_handler import catch_errors_in_class
from utils.helpers import class_runner, helper


@catch_errors_in_class
class BaseController:
    """Base class for all controllers. All controllers should inherit from this class."""

    def __init__(self, cmd_name: str, db: SqlDataStore, cmd_color: str):
        self.cmd_name = cmd_name
        self.db = db
        self.command_dict: dict[str, callable] = {}
        self.cmd_color = cmd_color

    def help(self) -> None:
        """Print available commands for the controller."""
        helper(self.command_dict)

    def run(self) -> None:
        """Run the controller."""
        class_runner(self.cmd_name, self.command_dict, self.cmd_color)

    def clear_screen(self):
        """Clear the screen."""
        print("\033[H\033[J")
