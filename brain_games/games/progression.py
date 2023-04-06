from typing import Dict

from brain_games.games.utils import generate_game_round_data, get_random_number

RULES = "What number is missing in the progression?"


def progression() -> Dict[str, str]:
    """
    Forms brain-progression game round data

    :return: brain-progression game round data
    :rtype: Dict[str, str]
    """
    step = get_random_number(1, 10)
    start = get_random_number(0, 40)
    progression_size = get_random_number(5, 10)
    end = start + step * progression_size
    progression_list = list(str(i) for i in range(start, end, step))
    correct_answer_index = get_random_number(0, progression_size - 1)
    correct_answer = progression_list[correct_answer_index]
    progression_list[correct_answer_index] = ".."
    question = " ".join(i for i in progression_list)
    return generate_game_round_data(RULES, question, str(correct_answer))
