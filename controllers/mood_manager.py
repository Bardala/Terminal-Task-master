from .base_controller import BaseController
from database.sql_data_store import SqlDataStore
from utils.error_handler import catch_errors
from utils.helpers import *
from database.sql_data_store import SqlDataStore
from utils.error_handler import catch_errors
from utils.helpers import *


class MyModeManager(BaseController):
    def __init__(self, db: SqlDataStore, cmd_name: str = "mood> "):
        super().__init__(cmd_name, db)
        self.command_dict: dict[str, callable] = {
            "add": self.add,
            "mood": self.mood,
            "clear": self.clear_screen,
            "help": self.help,
        }

    def help(self) -> None:
        helper(self.command_dict)

    def get_issues(self) -> list[dict[str, any]]:
        return self.db.get_issues()

    def add(self) -> None:
        print(">>> What is the issue?")
        issue_name: str = colored_input(">>")
        issue: dict[str, any] = {}
        if check_user_input(issue_name):
            return

        stored_issues: list[dict[str, any]] = self.get_issues()

        for stored_issue in stored_issues:
            if issue_name == stored_issue["issue"]:
                issue["id"] = stored_issue["id"]

        print(">>> What is the routine?")
        routine: str = colored_input(">>")
        if check_user_input(routine):
            return

        if "id" not in issue:
            self.db.add_issue(issue_name)
            issue = self.db.get_issue_by_name(issue_name)

        issue_routine: dict[str, any] = {
            "issue_id": issue["id"],
            "routine": routine,
        }
        self.db.add_issue_routine(issue_routine)

    def mood(self) -> None:
        issues: list[dict[str, any]] = self.db.get_issues()
        print(">>> What is your mood?")
        for issue in issues:
            print(f"{issue['id']}. {issue['issue']}")
        mood: str = colored_input(">>")
        if check_user_input(mood):
            return
        for issue in issues:
            if mood == issue["issue"]:
                routines: list[dict[str, any]] = self.db.get_issue_routines(issue["id"])
                for routine in routines:
                    print(f'- {routine["routine"]}')
                return
            else:
                print(">>> Invalid mood")

    def clear_screen(self) -> None:
        super().clear_screen()

    @catch_errors
    def run(self) -> None:
        class_runner(self.cmd_name, self.command_dict, db=self.db)
