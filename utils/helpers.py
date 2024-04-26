import sys
from colorama import Fore, init
from utils.error_handler import catch_errors

# * Constants
# Initialize colorama
init(autoreset=True)

# * Constants
MAIN_COMMAND_COLOR: str = Fore.GREEN
TODO_COMMAND_COLOR: str = Fore.BLUE
SETTINGS_COMMAND_COLOR: str = Fore.LIGHTBLUE_EX
PROJECT_COMMAND_COLOR: str = Fore.YELLOW
MOOD_COMMAND_COLOR: str = Fore.MAGENTA
INPUT_COLOR: str = Fore.CYAN
TODO_ID_COLOR: str = Fore.MAGENTA


@catch_errors
def command(string: str) -> str:
    """Returns the string in lowercase and stripped."""
    return string.strip().lower()


def Goodbye():
    print(Fore.LIGHTBLACK_EX + "Goodbye")


@catch_errors
def colored_input(prompt: str, prompt_color: str = Fore.GREEN) -> str:
    """Prints the prompt and returns the user input."""
    print(prompt_color + prompt, end="")
    user_input = input()
    return command(user_input)


@catch_errors
def class_runner(cmd_msg: str, command_dict: dict, cmd_color: str = Fore.GREEN) -> None:
    """Runs the command given by the user."""
    cmd = colored_input(cmd_msg, cmd_color)
    for command in command_dict:
        if command.startswith(cmd):
            if command == cmd:
                command_dict[command]()
                break
            print(Fore.LIGHTBLACK_EX + command)
            command_dict[command]()
            break
    else:
        if cmd == "":
            pass
        elif check_user_input(cmd):
            return
        else:
            print(Fore.RED + "Invalid command")
            print("'help' for list of commands")
    class_runner(cmd_msg, command_dict, cmd_color)


@catch_errors
def helper(command_dict: dict) -> None:
    """Prints the available commands for the current mode."""
    print("Available commands:")
    for command in command_dict:
        print(command)


@catch_errors
def check_user_input(input_task: str) -> bool:
    if input_task == "/":
        return True
    elif input_task == "":
        print(Fore.RED + "Task cannot be empty")
        return True
    elif input_task == "//":
        Goodbye()
        sys.exit(0)
    return False
