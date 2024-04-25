from colorama import Fore
import inspect


def catch_errors(func):
    """Function error handler"""

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if e == KeyboardInterrupt:
                print("\nGoodbye")
                exit()
            if str(e).startswith("UNIQUE constraint"):
                print(Fore.RED + "This value already exists")
            if str(e).startswith("invalid literal for int() with base 10"):
                print(Fore.RED + "Please enter a number")
            else:
                print(
                    Fore.RED + f"An error occurred",
                    Fore.LIGHTRED_EX + f"\n{e} \n{func.__name__}",
                    "failed",
                )

    return wrapper


def catch_errors_in_class(cls):
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        setattr(cls, name, catch_errors(method))
    return cls
