import inspect
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
    return string.strip().lower()


def colored_input(prompt, prompt_color=Fore.GREEN, input_color=Fore.CYAN):
    print(prompt_color + prompt, end="")
    user_input = input()
    return command(user_input)


def class_runner(cmd_msg, command_dict, cmd_color=Fore.GREEN, db=None):
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
    print("Available commands:")
    for command in command_dict:
        print(command)


# Todo: Move these functions to a separate file called error_handlers.py
def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if e == KeyboardInterrupt:
                print("\nGoodbye")
                exit()
            if str(e).startswith("UNIQUE constraint"):
                print(Fore.RED + "This value already exists")
            else:
                print(f"An error occurred: {e}")

    return wrapper


def catch_errors_in_class(cls):
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        setattr(cls, name, catch_errors(method))
    return cls
