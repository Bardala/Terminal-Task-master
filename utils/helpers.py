from os import system
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# * Constants
MAIN_COMMAND_COLOR = Fore.GREEN
TODO_COMMAND_COLOR = Fore.BLUE
PROJECT_COMMAND_COLOR = Fore.YELLOW
INPUT_COLOR = Fore.CYAN
TODO_ID_COLOR = Fore.MAGENTA


def command(string):
    """Returns the string in lowercase and stripped."""
    return string.strip().lower()


def colored_input(prompt, prompt_color=Fore.GREEN, input_color=Fore.CYAN):
    """Prints the prompt and returns the user input."""
    print(prompt_color + prompt, end="")
    user_input = input()
    return command(user_input)


def class_runner(cmd_msg, command_dict, cmd_color=Fore.GREEN, db=None):
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
        if cmd == "/":
            if cmd_msg == "bardala> ":  # main class
                print(Fore.LIGHTBLACK_EX + "Goodbye")
                db.close()
            return
        elif cmd == "":
            pass
        else:
            print(Fore.RED + "Invalid command")
            print("'help' for list of commands")
    class_runner(cmd_msg, command_dict, cmd_color, db)


def helper(command_dict):
    """Prints the available commands for the current mode."""
    print("Available commands:")
    for command in command_dict:
        print(command)


def check_backslash(input_task):
    if input_task == "/":
        return True
    elif input_task == "":
        print(Fore.RED + "Task cannot be empty")
        return True
    elif input_task == "//":
        system.exit()
    return False
