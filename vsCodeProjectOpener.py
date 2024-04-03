import subprocess
import os

from utils.helpers import PROJECT_COMMAND_COLOR, catch_errors, colored_input


# Todo: Switch this class to deal with all directories, not just VSCode
class VSCodeProjectOpener:
    def __init__(self, db):
        self.db = db

    def add_project(self, name, directory):
        if not os.path.exists(directory):
            raise ValueError(f"No such directory: {directory}")
        self.db.add_project(name, directory)

    def open_project(self, name):
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

    def delete_project(self, name):
        self.db.delete_project_by_name(name) if self._check_is_project(name) else None

    # todo
    def update_project_dir(self, name, new_directory):
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

    def delete(self, name):
        self.delete_project(name)

    @catch_errors
    def run_project_mode(self):
        cmd = colored_input("project> ", PROJECT_COMMAND_COLOR)
        if cmd == "add":
            name = colored_input("Enter project name: ")
            if name == "/":
                return
            directory = colored_input("Enter project directory: ")
            if directory == "/":
                return
            self.add_project(name, directory)
        elif cmd == "open":
            name = colored_input("Enter project name: ")
            self.open_project(name)
        elif cmd == "list":
            self.list_projects()
        elif cmd == "delete":
            name = colored_input("Enter project name: ")
            self.delete(name)
        elif cmd == "update":
            name = colored_input("Enter project name: ")
            new_directory = colored_input("Enter new directory: ")
            self.update_project_dir(name, new_directory)
        elif cmd == "/":
            return
        else:
            print("Invalid command")
            print("Commands: add, open, list, /")
        self.run_project_mode()
