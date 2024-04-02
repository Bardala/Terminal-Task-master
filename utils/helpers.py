from colorama import Fore, Style


def command(string):
    return string.strip().lower()


def stdin():
    print(Fore.YELLOW + "bardala> ", end="")

    # Get the user input in cyan color
    print(Fore.CYAN, end="")  # ?This statement doesn't work
    user_input = input()

    print(Style.RESET_ALL, end="")
    return user_input.strip()
