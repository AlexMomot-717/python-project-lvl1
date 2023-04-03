#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.gcd import gcd


def main() -> None:
    """
    Executes brain-gcd game
    """
    run_game(gcd)


if __name__ == "__main__":
    main()
