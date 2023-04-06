#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.progression import progression


def main() -> None:
    """
    Executes brain-progression game
    """
    run_game(progression)


if __name__ == "__main__":
    main()
