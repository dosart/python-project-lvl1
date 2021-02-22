#!/usr/bin/env python3
"""Prime game script."""

from brain_games.engine import run_game
from brain_games.games import prime
from brain_games import cli


def main():
    """Prime game script."""
    run_game(prime, cli)


if __name__ == '__main__':
    main()
