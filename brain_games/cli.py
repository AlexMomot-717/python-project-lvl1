import prompt


def welcome_user() -> None:
    """Requires a username, returns user greeting"""
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
