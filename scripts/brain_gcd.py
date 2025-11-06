#!/usr/bin/env python3
"""Игра НОД (Наибольший общий делитель)"""

from games_project_bolzhatov.engine import run_game
from games_project_bolzhatov.games.gcd_game import generate_question


def main():
    """Запуск игры НОД"""
    run_game(
        game_description="Find the greatest common divisor of given numbers.",
        generate_question=generate_question
    )


if __name__ == '__main__':
    main()
