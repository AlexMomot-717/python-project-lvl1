from typing import Dict

from brain_games.games.utils import generate_game_round_data, get_random_number

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
PRIME_SET = frozenset(
    {
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    }
)


def prime() -> Dict[str, str]:
    """
    Forms brain-prime game round data

    :return: brain-prime game round data
    :rtype: Dict[str, str]
    """
    number = get_random_number(1, 100)
    correct_answer = "yes" if number in PRIME_SET else "no"
    question = str(number)
    return generate_game_round_data(RULES, question, correct_answer)
