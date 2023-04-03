from random import randint
from typing import Dict


def get_random_number(bottom: int, ceiling: int) -> int:
    return randint(bottom, ceiling)


def generate_game_round_data(
    rules: str, question: str, correct_answer: str
) -> Dict[str, str]:
    task_params = {
        "rules": rules,
        "question": question,
        "correct_answer": correct_answer,
    }
    return task_params
