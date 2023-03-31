from random import randint
from typing import Dict


def even() -> Dict[str, str]:
    """
    Forms brain-even game round data

    :return: brain-even game round data
    :rtype: Dict[str, str]
    """
    num = randint(0, 100)
    correct_answer = "yes" if num % 2 == 0 else "no"
    task_params = {
        "rules": 'Answer "yes" if the number is even, otherwise answer "no".',
        "question": str(num),
        "correct_answer": correct_answer,
    }
    return task_params
