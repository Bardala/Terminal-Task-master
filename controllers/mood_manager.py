from utils.error_handler import catch_errors
from utils.helpers import *


class MyModeManager:
    def __init__(self, db):
        self.db = db
        self.cmd_name = "mood> "
        self.command_dict = {
            "add": self.add,
            "mood": self.mood,
            "help": self.help,
        }

    def help(self):
        helper(self.command_dict)

    def get_issues(self):
        return self.db.get_issues()

    def add(self):
        print(">>> What is the issue?")
        issue_name = colored_input(">>")
        issue = {}
        if check_backslash(issue_name):
            return

        stored_issues = self.get_issues()

        for stored_issue in stored_issues:
            if issue_name == stored_issue["issue"]:
                issue["id"] = stored_issue["id"]

        print(">>> What is the routine?")
        routine = colored_input(">>")
        if check_backslash(routine):
            return

        if "id" not in issue:
            self.db.add_issue(issue_name)
            issue = self.db.get_issue_by_name(issue_name)

        issue_routine = {
            "issue_id": issue["id"],
            "routine": routine,
        }
        self.db.add_issue_routine(issue_routine)

    def mood(self):
        issues = self.db.get_issues()
        print(">>> What is your mood?")
        for issue in issues:
            print(f"{issue['id']}. {issue['issue']}")
        mood = colored_input(">>")
        if check_backslash(mood):
            return
        for issue in issues:
            if mood == issue["issue"]:
                routines = self.db.get_issue_routines(issue["id"])
                for routine in routines:
                    print(f'- {routine["routine"]}')
                return
            else:
                print(">>> Invalid mood")

    @catch_errors
    def run_mood_mode(self):
        class_runner(self.cmd_name, self.command_dict, db=self.db)
