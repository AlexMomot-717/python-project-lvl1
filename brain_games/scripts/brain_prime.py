#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.prime import prime


def main() -> None:
    """
    Executes brain-prime game
    """
    run_game(prime)


if __name__ == "__main__":
    main()
