"""Prime game engine."""

from random import randint

from brain_games.global_constants import QUESTION, ANSWER


def get_description():
    """Return description of game.

    Returns:
        description(string): description of game
    """
    return 'Answer "yes" if number prime otherwise answer "no".'


def get_count_rounds():
    """Return count of game round.

    Returns:
        num (int): count of game round
    """
    return 3


def get_challenge():
    """Prime game Q&A generation.

    generate random Number and check if a Number is Prime

    Returns:
        key QUESTION (string): number;
        key ANSWER (string): Prime status
    """
    num = randint(_min, _max)

    answer = 'yes' if _is_prime(num) else 'no'
    question = '{0}'.format(num)

    return {QUESTION: question, ANSWER: answer}


def _min():
    return 1


def _max():
    return 20


def _is_prime(num):
    """Prime number check.

    Args:
        num (int): number to check

    Returns:
        bool: True if number is prime
    """
    if num < 2:
        return False
    index = 2
    while index <= num // 2:
        if num % index == 0:
            return False
        index += 1
    return True
