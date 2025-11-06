#!/usr/bin/env python3
"""Игра Калькулятор"""

from games_project_bolzhatov.engine import run_game
from games_project_bolzhatov.games.calc_game import generate_question


def main():
    """Запуск игры Калькулятор"""
    run_game(
        game_description="What is the result of the expression?",
        generate_question=generate_question
    )


if __name__ == '__main__':
    main()
