import random
from math import gcd


def generate_question():
    """Генерирует два случайных числа и возвращает вопрос и НОД"""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    question = f"{num1} {num2}"
    correct_answer = gcd(num1, num2)
    
    return question, str(correct_answer)
