#!/usr/bin/env python3
"""Brain game script."""

from brain_games.cli import welcome_user, print_message


def main():
    """Print 'Welcome to the Brain Games!'."""
    print_message('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
