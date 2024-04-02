from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# * Constants
# Colors
MAIN_COMMAND_COLOR = Fore.GREEN
TODO_COMMAND_COLOR = Fore.BLUE
INPUT_COLOR = Fore.CYAN
TODO_ID_COLOR = Fore.MAGENTA


def command(string):
    return string.strip().lower()


def colored_input(
    prompt,
    prompt_color=Fore.GREEN,
    input_color=Fore.BLACK,
):
    print(prompt_color + prompt, end="")

    user_input = input()

    # # Print the user input in the specified color
    # print(input_color + user_input)

    return command(user_input)
