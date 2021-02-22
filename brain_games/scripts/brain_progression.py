#!/usr/bin/env python3
"""Progression game script."""


from brain_games.engine import run_game
from brain_games.games import progression
from brain_games import cli


def main():
    """Progression game script."""
    run_game(progression, cli)


if __name__ == '__main__':
    main()
