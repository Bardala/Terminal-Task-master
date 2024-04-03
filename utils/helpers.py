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
