#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.even import game


def main() -> None:
    name = welcome_user()
    game(name)


if __name__ == "__main__":
    main()
