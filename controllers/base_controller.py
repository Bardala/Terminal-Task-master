from abc import ABC, abstractmethod
from database.sql_data_store import SqlDataStore


class BaseController(ABC):
    """Base class for all controllers. All controllers should inherit from this class."""

    def __init__(self, cmd_name: str, db: SqlDataStore):
        self.cmd_name = cmd_name
        self.db = db
        self.command_dict: dict[str, callable] = {}

    @abstractmethod
    def help(self) -> None:
        """Print available commands for the controller."""
        pass

    @abstractmethod
    def run(self) -> None:
        """Run the controller."""
        pass
