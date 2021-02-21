#!/usr/bin/env python3
"""Calc game script."""

from brain_games.engine import run_game
from brain_games.games import calc
from brain_games import cli


def main():
    """Calc game script."""
    run_game(calc, cli)


if __name__ == '__main__':
    main()
