import random

from prompt import string


def game(name: str) -> None:
    count = 0
    while count < 3:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        num = random.randint(0, 100)
        correct_answer = "yes" if num % 2 == 0 else "no"
        print(f"Question: {num}")
        answer = string("Your answer: ")
        if correct_answer == answer:
            print("Correct!")
            count += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
                f"\nLet's try again, {name}!'"
            )
            return
    print(f"Congratulations, {name}!")
