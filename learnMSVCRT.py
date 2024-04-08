import msvcrt
from colorama import Fore


class SimpleCommandRunner:
    def __init__(self):
        self.commands = ["add", "open", "list", "delete", "update"]

    def add(self):
        print("Add command executed")

    def open(self):
        print("Open command executed")

    def list(self):
        print("List command executed")

    def delete(self):
        print("Delete command executed")

    def update(self):
        print("Update command executed")

    def run_project_mode(self):
        print("project> ", end="", flush=True)
        cmd = ""
        while True:
            if msvcrt.kbhit():
                char = msvcrt.getche().decode("utf-8")  # Read a key
                if char == "\r":  # Enter key pressed
                    break
                elif char == "\b":  # Backspace key pressed
                    cmd = cmd[:-1]
                elif char == "\t":  # Tab key pressed
                    nearest_command = next(
                        (
                            command
                            for command in self.commands
                            if command.startswith(cmd)
                        ),
                        None,
                    )
                    if nearest_command:
                        cmd = nearest_command
                        print("\r" + " " * 80 + "\r", end="", flush=True)  # Clear line
                        print("project> " + cmd, end="", flush=True)
                else:
                    cmd += char
                nearest_command = next(
                    (command for command in self.commands if command.startswith(cmd)),
                    None,
                )
                if nearest_command:
                    print("\r" + " " * 80 + "\r", end="", flush=True)  # Clear line
                    print(
                        "project> " + cmd + Fore.GREEN + nearest_command[len(cmd) :],
                        end="",
                        flush=True,
                    )
        print(Fore.RESET)  # Reset color

        command_dict = {
            "add": self.add,
            "open": self.open,
            "list": self.list,
            "delete": self.delete,
            "update": self.update,
        }

        if cmd in command_dict:
            command_dict[cmd]()
        else:
            print(f"Unknown command: {cmd}")


class LearnMSVCRT:
    def test(self):
        print("Press any key to continue...")
        while not msvcrt.kbhit():
            pass  # Wait for a keypress

        user_input = input(
            "Enter the first 3 letters of a word, and then enter tab, and I will suggest it"
        )
        key = msvcrt.getch()  # Read the key that was pressed
        print(f"You pressed: {key}")


runner = LearnMSVCRT()
runner.test()
