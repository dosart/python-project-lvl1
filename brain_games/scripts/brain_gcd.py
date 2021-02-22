#!/usr/bin/env python3
"""GCD game script."""

from brain_games.engine import run_game
from brain_games.games import gcd
from brain_games import cli


def main():
    """GCD game script."""
    run_game(gcd, cli)


if __name__ == '__main__':
    main()
