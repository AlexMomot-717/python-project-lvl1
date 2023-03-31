from prompt import string


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    user_name = string("May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name


def tell_rules(rules: str) -> None:
    print(rules)


def ask_question(expression: str) -> None:
    print(f"Question: {expression}")


def get_answer() -> str:
    return string("Your answer: ")


def confirm_answer() -> None:
    print("Correct!")


def loose(answer: str, correct_answer: str, user_name: str) -> None:
    print(
        f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
        f"\nLet's try again, {user_name}!'"
    )


def congratulate(user_name: str) -> None:
    print(f"Congratulations, {user_name}!")
