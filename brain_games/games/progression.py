"""Progression game engine."""

from random import randint

from brain_games.global_constants import QUESTION, ANSWER


def get_description():
    """Return description of game.

    Returns:
        description(string): description of game
    """
    return 'What number is missing in the progression?'


def get_count_rounds():
    """Return count of game round.

    Returns:
        num (int): count of game round
    """
    return 3


def get_challenge():
    """Progression game Q&A generation.

    It forms an arithmetic progression,
    replacing one of the numbers with two points.

    Returns:
        question{str} : arithmetic progression;
        answer{str} : hidden number
    """
    start = randint(_start_min(), _start_max())
    step = randint(_step_min(), _step_max())
    progression = [(start + (element * step))
                   for element in range(_progression_length())]

    hidden_element_index = randint(0, _progression_length() - 1)
    answer = str(progression[hidden_element_index])
    progression[hidden_element_index] = '..'

    question = ' '.join(str(element) for element in progression)

    return {QUESTION: question, ANSWER: answer}


def _start_min():
    return 1


def _start_max():
    return 10


def _step_min():
    return 1


def _step_max():
    return 10


def _progression_length():
    return 10
