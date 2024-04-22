import subprocess
import os
from colorama import Fore
from .base_controller import BaseController
from database.sql_data_store import SqlDataStore
from utils.error_handler import *
from utils.helpers import *


# Todo: Covert project with item, and use with the new db updates, folders and item_folders.
# Todo: Switch this class to deal with all directories, not just VSCode
@catch_errors_in_class
class VSCodeProjectOpener(BaseController):
    def __init__(self, db: SqlDataStore, cmd_name: str = "project> "):
        super().__init__(cmd_name, db)
        self.command_dict: dict[str, callable] = {
            "add": self.add_project,
            "open": self.open_project,
            "list": self.list_projects,
            "ls": self.list_projects,
            "show": self.list_projects,
            "delete": self.delete_project,
            "update": self.update_project_dir,
            "ps": self.power_shell,
            "cmd": self.command_prompt,
            "bash": self.bash,
            "help": self.help,
        }

    def help(self) -> None:
        helper(self.command_dict)

    def add_project(self) -> None:
        name = colored_input("Enter project name: ")
        print(Fore.GREEN + "Enter project dir: ", end="")
        directory = input().strip()
        if not os.path.exists(directory):
            raise ValueError(f"No such directory: {directory}")
        if name != "/" and directory != "/":
            self.db.add_project(name, directory)

    def open_project(self) -> None:
        name = colored_input("Enter project name: ")
        project = self.db.get_project_by_name(name)
        if project:
            directory = project[2]
            # subprocess.Popen(["code", directory])
            subprocess.run(["code", directory], shell=True)

    def _check_is_project(self, name: str) -> bool:
        project = self.db.get_project_by_name(name)
        if not project:
            print(f"No project with name: {name}")
            return False
        return True

    def update_project_dir(self) -> None:
        name = colored_input("Enter project name: ")
        new_directory = colored_input("Enter new directory: ")
        if not os.path.exists(new_directory):
            raise ValueError(f"No such directory: {new_directory}")
        self.db.update_project_by_name(name, new_directory)

    def list_projects(self) -> None:
        projects = self.db.get_all_projects()
        if not projects:
            print("No projects found")
            return
        for project in projects:
            print(f"{project[1]}: {project[2]}")

    def delete_project(self) -> None:
        name = colored_input("Enter project name: ")
        self.db.delete_project_by_name(name) if self._check_is_project(name) else None

    def cli(self, cmd_name: str) -> tuple[str, str]:
        """This function will handle the command line interface for the user."""
        # this variable will be in this shape: code mine, ii table, ii book, ls dir...
        user_input = colored_input(f"{cmd_name}> ", Fore.LIGHTCYAN_EX)
        command = user_input.split(" ")[0]
        item = user_input.split(" ")[1] if len(user_input.split(" ")) > 1 else None
        db_item = self.db.get_project_by_name(item)
        item = db_item[2] if db_item else item
        return command, item

    def command_prompt(self) -> None:
        """This function will handle the command prompt for the user."""
        command, item = self.cli("cmd")
        if check_user_input(command):
            return
        subprocess.runt([command, item], shell=True)
        return self.command_prompt()

    # ?Be aware this function may not work well with linux subsystem on windows because of the way it handles the paths.
    # !The program needs more testing with bash, there are some issues.
    def bash(self) -> None:
        """This function will handle the bash commands for the user."""
        command, item = self.cli("bash")
        if check_user_input(command):
            return
        subprocess.run(["bash", "-c", f"{command} {item}"])
        return self.bash()

    # Todo: Implement the PowerShell commands with all the features of the current program.
    def power_shell(self) -> None:
        """This function has the ability to implement PowerShell commands with current program features."""
        command, item = self.cli("ps")
        if check_user_input(command):
            return
        subprocess.run(["powershell", "-Command", f"{command} {item}"], shell=True)
        return self.power_shell()

    @catch_errors
    def run(self) -> None:
        class_runner(self.cmd_name, self.command_dict, PROJECT_COMMAND_COLOR)
