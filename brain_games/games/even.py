"""Even game engine."""

from random import randint

from brain_games.global_constants import QUESTION, ANSWER


def _min():
    return 1


def _max():
    return 30


def get_description():
    """Return description of game.

    Returns:
        description(string): description of game
    """
    return "Answer 'yes' if number even otherwise answer 'no'."


def get_count_rounds():
    """Return count of game round.

    Returns:
        num (int): count of game round
    """
    return 3


def get_challenge():
    """Even game Q&A generation.

    generate random Number and check if a Number is Even

    Returns:
        dictionary:
            key QUESTION (string) : question of challenge;
            key ANSWER (string): answer of challenge
    """
    num = randint(_min(), _max())
    answer = 'no' if num % 2 else 'yes'
    question = '{0}'.format(num)

    return {QUESTION: question, ANSWER: answer}
