from colorama import Fore
import inspect


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
