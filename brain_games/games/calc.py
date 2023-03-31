from random import choice, randint
from typing import Dict

OPERATORS = ["+", "-", "*"]


def calc() -> Dict[str, str]:
    """
    Forms brain-calc game round data

    :return: brain-calc game round data
    :rtype: Dict[str, str]
    """
    num1 = randint(0, 20)
    num2 = randint(0, 20)
    operator_symbol = choice(OPERATORS)
    question = f"{num1} {operator_symbol} {num2}"
    if operator_symbol == "+":
        correct_answer = num1 + num2
    elif operator_symbol == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    task_params = {
        "rules": "What is the result of the expression?",
        "question": question,
        "correct_answer": str(correct_answer),
    }
    return task_params
