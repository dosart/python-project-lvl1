"""GCD game engine."""

from random import randint
from math import gcd

from brain_games.global_constants import QUESTION, ANSWER


def get_description():
    """Return description of game.

    Returns:
        description(string): description of game
    """
    return 'Find the greatest common divisor of given numbers.'


def get_count_rounds():
    """Return count of game round.

    Returns:
        num (int): count of game round
    """
    return 3


def get_challenge():
    """GCD game Q&A generation.

    generate two random Numbers
    and calculate greatest common divider for them

    Returns:
        key QUESTION (string):  Numbers;
        key ANSWER (string): greatest common divider
    """
    num1 = randint(_min(), _max())
    num2 = randint(_min(), _max())

    answer = str(gcd(num1, num2))
    question = '{0} {1}'.format(num1, num2)

    return {QUESTION: question, ANSWER: answer}


def _min():
    return 1


def _max():
    return 30
