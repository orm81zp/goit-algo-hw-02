""" Модуль по перевірці рядка від користувача на палнідром """

from collections import deque


class UnexpectedException(Exception):
    """Класс перехоплення загальних помилок"""


def palindrome(string):
    """
    Перевіряє рядок на паліндром

    Params:
        - text (str): рядок для перевірки

    Return: bool
    """

    # прибираємо пробіли
    string = string.replace(" ", "")
    queue: deque[str] = deque(string)
    while len(queue) > 1:
        first_character = queue.popleft()
        last__character = queue.pop()
        # приводимо до нижнього регістру
        if first_character.lower() != last__character.lower():
            return False

    return True


def info():
    """Виводить інформації"""
    print("Для виходу введіть exit")
    print()


def main():
    """Запускає процесс перевірки рядка від користовача на паліндром"""
    is_running = True
    print("Супер паліндромом перевірка v1")
    info()

    while is_running:
        try:
            user_input = input("Введіть рядок на перевірку: ").strip()
            cmd = user_input.lower()

            if cmd in ["вихід", "exit", "учше"]:
                print("До побачення! Спокійного вам дня!")
                is_running = False
            else:
                is_palindrome = palindrome(user_input)
                if is_palindrome:
                    print(f'Рядок "{user_input}" є паліндромом!')
                else:
                    print("Рядок не паліндром :(")
        except UnexpectedException as err:
            print("О, це все! Сталася біда!")
            print(err)


if __name__ == "__main__":
    main()
