from typing import Callable, Dict

from brain_games.cli import (
    ask_question,
    confirm_answer,
    congratulate,
    get_answer,
    loose,
    tell_rules,
    welcome_user,
)

GAME_ROUNDS_NUMBER = 3


def run_game(func: Callable[[], Dict[str, str]]) -> None:
    """
    Implements brain game algorithm

    :param func: function that returns game round data
    :type func: Callable[[], Dict[str, str]]
    """
    user_name = welcome_user()
    for __ in range(GAME_ROUNDS_NUMBER):
        task_params = func()
        tell_rules(task_params["rules"])
        ask_question(task_params["question"])
        correct_answer = task_params["correct_answer"]
        answer = get_answer()
        if correct_answer == answer:
            confirm_answer()
        else:
            loose(answer, correct_answer, user_name)
            return
    congratulate(user_name)
