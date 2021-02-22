"""Command line interface for brain games."""

import prompt


def welcome_user():
    """Welcome dialog."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))


def print_message(message):
    """Print message in console.
    
    Args:
        message (string): message for output
    """
    print(message)


def print_description(description):
    """Print description of game in console.

    Args:
        description (string): description of game
    """
    print('{0}\n'.format(description))


def print_hello(user_name):
    """Print Hello user_name in consile.

    Args:
        user_name (string): name of user
    """
    print('Hello, {0}!\n'.format(user_name))


def print_wrong_answer(user_answer, right_answer):
    """Print message of wrong answer.

    Args:
        user_answer (string): wrong answer of user
        right_answer (string): right answer of game
    """
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
          user_answer, right_answer))


def print_try_again(user_name):
    """Print massage 'try again' in console.

    Args:
        user_name (string): name of user
    """
    print("Let's try again, {0}!".format(user_name))


def print_congratulations(user_name):
    """Print congratulations of user in console.

    Args:
        user_name (string): name of user
    """
    print('Congratulations, {0}'.format(user_name))


def print_correct():
    """Print correct in console."""
    print('Correct!')


def get_user_name():
    """Return eser name from console.

    Returns:
        user_name (string): name of user from console
    """
    return prompt.string('May I have your name? ')


def get_answer(question):
    """Return input of user from console.

    Args:
        question (string) : question

    Returns:
        answer (string): answer of user
    """
    return prompt.string('Question: {0}\nYour answer: '.format(question))
