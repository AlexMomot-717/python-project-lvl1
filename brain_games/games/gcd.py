from math import gcd as m_gcd
from typing import Dict

from brain_games.games.utils import generate_game_round_data, get_random_number

RULES = "Find the greatest common divisor of given numbers."


def gcd() -> Dict[str, str]:
    """
    Forms brain-gcd game round data

    :return: brain-gcd game round data
    :rtype: Dict[str, str]
    """
    num1 = get_random_number(1, 100)
    num2 = get_random_number(1, 100)
    question = f"{num1} {num2}"
    correct_answer = m_gcd(num1, num2)
    return generate_game_round_data(RULES, question, str(correct_answer))
