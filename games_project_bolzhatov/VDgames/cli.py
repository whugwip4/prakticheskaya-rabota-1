import prompt


def welcome_user():
    """Приветствует пользователя и запрашивает его имя."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
