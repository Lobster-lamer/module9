from consoleTextStyle import ConsoleTextStyle as CoTeSt
import random


class MysticBall:
    def __init__(self, *words_to_choice):
        self.words_to_choice = words_to_choice

    def __call__(self):
        return random.choice(self.words_to_choice)


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, "w", encoding="utf-8") as file:
            for data_line in data_set:
                file.write(str(data_line) + "\n")
        CoTeSt.colorful_text(f"Запись в файл {CoTeSt.colorful_str(file_name, CoTeSt.Color.PURPLE)}"
                             f"{CoTeSt.Color.GREEN} произведена успешно", CoTeSt.Color.GREEN)

    return write_everything


if __name__ == "__main__":
    #  Lambda-функция:
    CoTeSt.colorful_text("Вывод задания на Lambda-функцию", CoTeSt.Color.CYAN)
    first = 'Мама мыла раму'
    second = 'Рамена мало было'

    print(list(map(lambda f, s: f == s, first, second)))

    #  Замыкание:
    CoTeSt.colorful_text("\nВывод задания на замыкание", CoTeSt.Color.CYAN)
    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

    #  Метод __call__:
    CoTeSt.colorful_text("\nВывод задания на использование метода __call__ класса", CoTeSt.Color.CYAN)

    first_ball = MysticBall("Да", "Нет", "Наверное")
    print(first_ball())
    print(first_ball())
    print(first_ball())
