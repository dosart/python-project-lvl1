"""Brain Games Engine."""

from brain_games.global_constants import ANSWER, QUESTION, INTRO


def run_game(game, io):
    """Brain Games Engine.

    Executing game process

    Args:
        game (object): create game question and answer
        io (object): input/output environment
    """
    io.print_message(INTRO)

    user_name = io.get_user_name()
    io.print_hello(user_name)

    io.print_description(game.get_description())

    for _ in range(game.get_count_rounds()):
        challenge = game.get_challenge()
        game_question = challenge[QUESTION]
        right_answer = challenge[ANSWER]

        user_answer = io.get_answer(game_question)
        if user_answer == right_answer:
            io.print_correct()
        else:
            io.print_wrong_answer(user_answer, right_answer)
            io.print_try_again(user_name)
            return
    io.print_congratulations(user_name)
