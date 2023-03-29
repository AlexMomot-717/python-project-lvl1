from prompt import string


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    return name
