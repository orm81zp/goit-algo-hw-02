""" Модуль по прийому та обробці заявок від користувача """

from queue import Queue
from uuid import uuid4
from time import sleep


class UnexpectedException(Exception):
    """Класс перехоплення загальних помилок"""


class Request:
    """Класс для створення заявок"""

    def __init__(self, text):
        self.id = uuid4()
        self.text = text

    def __str__(self) -> str:
        return f"#{self.id} {self.text}"

    def __repr__(self) -> str:
        return f"Request #{self}"


# Створити чергу заявок
queue: Queue[Request] = Queue()


def generate_request(text):
    """
    Створює нову заявку та додає її до черги

    Params:
        - request (str)

    Return None
    """

    new_request = Request(text)
    queue.put(new_request)
    print(new_request)
    print(f"Заявка #{new_request.id} створена.")


def process_requests():
    """
    Обробляє заявки з черги

    Return None
    """

    if not queue.empty():
        request = queue.get()
        print(f"Обробка заявки {request}...")
        sleep(1)
        print("Успішно!")
    else:
        print("Черга пуста та сумна...")


def info():
    """Виводить інформації"""
    print("Для виходу введіть exit")
    print()


def main():
    """Запускає процесс створення на обробки заявок від користувача"""
    is_running = True
    print("Супер Менеджер заявок v1")
    info()

    while is_running:
        try:
            user_input = input("Чим можу бути вам корисний? ").strip()
            cmd = user_input.lower()

            if cmd in ["вихід", "exit", "учше"]:
                print("До побачення! Спокійного вам дня!")
                is_running = False
            else:
                if user_input:
                    generate_request(user_input)
                process_requests()
        except UnexpectedException as err:
            print("О, це все! Сталася біда!")
            print(err)


if __name__ == "__main__":
    main()
