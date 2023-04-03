from random import choice
from typing import Dict

from brain_games.games.utils import generate_game_round_data, get_random_number

OPERATORS = ["+", "-", "*"]
RULES = "What is the result of the expression?"


def calc() -> Dict[str, str]:
    """
    Forms brain-calc game round data

    :return: brain-calc game round data
    :rtype: Dict[str, str]
    """
    num1 = get_random_number(0, 20)
    num2 = get_random_number(0, 20)
    operator_symbol = choice(OPERATORS)
    question = f"{num1} {operator_symbol} {num2}"
    if operator_symbol == "+":
        correct_answer = num1 + num2
    elif operator_symbol == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return generate_game_round_data(RULES, question, str(correct_answer))
