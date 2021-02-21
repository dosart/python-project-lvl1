"""Calc game engine."""

from random import randint, choice
from operator import add, mul, sub

from brain_games.global_constants import QUESTION, ANSWER


def get_description():
    """Return description of game.

    Returns:
        description(string): description of game
    """
    return 'What is the result of the expression?'


def get_count_rounds():
    """Return count of game round.

    Returns:
        num (int): count of game round
    """
    return 3


def get_challenge():
    """Calc game Q&A generation.

    generate two random numbers
    and calculate result of random operation

    Returns:
        dictionary:
            key QUESTION (string) : operation description;
            key ANSWER (string) : result of operation
    """
    num1 = randint(_min(), _max())
    num2 = randint(_min(), _max())
    operation, sign = _get_operators(choice)

    answer = str(operation(num1, num2))
    question = '{0} {1} {2}'.format(num1, sign, num2)

    return {QUESTION: question, ANSWER: answer}


def _min():
    return 1


def _max():
    return 30


def _get_operators(selector):
    operators = [(add, '+'), (sub, '-'), (mul, '*')]
    return selector(operators)
