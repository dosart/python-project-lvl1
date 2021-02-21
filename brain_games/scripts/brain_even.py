#!/usr/bin/env python3
"""Even game script."""

from brain_games.engine import run_game
from brain_games.games import even
from brain_games import cli


def main():
    """Even game script."""
    run_game(even, cli)


if __name__ == '__main__':
    main()
