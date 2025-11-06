import random


def generate_question():
    """Генерирует случайный пример и возвращает вопрос и правильный ответ"""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    
    question = f"{num1} {operator} {num2}"
    
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:  # operator == '*'
        correct_answer = num1 * num2
    
    return question, str(correct_answer)
