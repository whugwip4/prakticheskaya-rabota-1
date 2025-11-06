"""Движок для игр"""


def run_game(game_description, generate_question, rounds=3):
    """
    Запускает игру на несколько раундов.
    
    Args:
        game_description: Описание игры, показывается в начале
        generate_question: Функция, которая генерирует вопрос и ответ
        rounds: Количество раундов (по умолчанию 3)
    """
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_description)
    
    correct_answers = 0
    
    for _ in range(rounds):
        question, correct_answer = generate_question()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f'Congratulations, {name}!')
