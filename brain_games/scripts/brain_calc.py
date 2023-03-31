#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.calc import calc


def main() -> None:
    """
    Executes brain-calc game
    """
    run_game(calc)


if __name__ == "__main__":
    main()
