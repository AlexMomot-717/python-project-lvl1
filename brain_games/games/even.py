from typing import Dict

from brain_games.games.utils import generate_game_round_data, get_random_number

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def even() -> Dict[str, str]:
    """
    Forms brain-even game round data

    :return: brain-even game round data
    :rtype: Dict[str, str]
    """
    num = get_random_number(0, 100)
    correct_answer = "yes" if num % 2 == 0 else "no"
    question = str(num)
    return generate_game_round_data(RULES, question, correct_answer)
