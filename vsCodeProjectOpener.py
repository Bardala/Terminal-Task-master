import subprocess
import os
from colorama import Fore
from utils.helpers import (
    PROJECT_COMMAND_COLOR,
    catch_errors,
    catch_errors_in_class,
    colored_input,
)


# Todo: Switch this class to deal with all directories, not just VSCode
@catch_errors_in_class
class VSCodeProjectOpener:
    def __init__(self, db):
        self.db = db
        self.command_dict = {
            "add": self.add_project,
            "open": self.open_project,
            "list": self.list_projects,
            "ls": self.list_projects,
            "show": self.list_projects,
            "delete": self.delete_project,
            "update": self.update_project_dir,
        }

    def add_project(self):
        name = colored_input("Enter project name: ")
        print(Fore.GREEN + "Enter project dir: ", end="")
        directory = input().strip()
        if name != "/" and directory != "/":
            self.add_project(name, directory)
        if not os.path.exists(directory):
            raise ValueError(f"No such directory: {directory}")
        self.db.add_project(name, directory)

    def open_project(self):
        name = colored_input("Enter project name: ")
        project = self.db.get_project_by_name(name)
        if project:
            directory = project[2]
            # subprocess.Popen(["code", directory])
            subprocess.run(["code", directory], shell=True)

    def _check_is_project(self, name):
        project = self.db.get_project_by_name(name)
        if not project:
            print(f"No project with name: {name}")
            return False
        return True

    # todo
    def update_project_dir(self):
        name = colored_input("Enter project name: ")
        new_directory = colored_input("Enter new directory: ")
        if not os.path.exists(new_directory):
            raise ValueError(f"No such directory: {new_directory}")
        self.db.update_project_by_name(name, new_directory)

    def list_projects(self):
        projects = self.db.get_all_projects()
        if not projects:
            print("No projects found")
            return
        for project in projects:
            print(f"{project[1]}: {project[2]}")

    def delete_project(self, name):
        name = colored_input("Enter project name: ")
        self.db.delete_project_by_name(name) if self._check_is_project(name) else None

    @catch_errors
    def run_project_mode(self):
        cmd = colored_input("project> ", PROJECT_COMMAND_COLOR)
        # todo: if cmd is a substring of a command, it will still run that command

        for command in self.command_dict:
            if command in cmd:
                self.command_dict[command]()
                break
        else:  # This else block runs when the for loop doesn't break
            if cmd == "/":
                return
            else:
                print(Fore.RED + "Invalid command", end="")
                print(
                    Fore.BLUE + "Commands: add, open, list, delete, update, /", end="\n"
                )
        self.run_project_mode()
