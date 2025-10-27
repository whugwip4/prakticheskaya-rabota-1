import random


def main():
    """
    Игра "Проверка на чётность"
    - Показываем случайное число
    - Пользователь отвечает: yes (чётное) или no (нечётное)
    - 3 правильных ответа подряд = победа
    - Любая ошибка = конец игры
    """
    print("🎮 Добро пожаловать в игру 'Проверка на чётность'!")
    print("Ответьте 'yes' если число чётное, 'no' если нечётное.")
    print("Нужно дать 3 правильных ответа подряд!\n")

    correct_count = 0

    while correct_count < 3:
        number = random.randint(1, 100)
        print(f"Число: {number}")

        user_answer = input("Ваш ответ (yes/no): ").strip().lower()

        is_even = number % 2 == 0
        correct_answer = "yes" if is_even else "no"

        if user_answer == correct_answer:
            correct_count += 1
            print(f"✅ Правильно! Счёт: {correct_count}/3\n")
        else:
            print(f"❌ Ошибка! Правильный ответ: {correct_answer}")
            print("🔴 Игра окончена!\n")
            return

    print("🎉 Поздравляем! Вы выиграли!")
