#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.even import even


def main() -> None:
    """
    Executes brain-even game
    """
    run_game(even)


if __name__ == "__main__":
    main()
