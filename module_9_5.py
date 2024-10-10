from consoleTextStyle import ConsoleTextStyle as CoTeSt


class StepValueError(ValueError):
    def __init__(self, message):
        self.message = message


class CountUpError(Exception):
    def __init__(self, message):
        self.message = message


class CountDownError(Exception):
    def __init__(self, message):
        self.message = message


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if self.step == 0:
            raise StepValueError("Шаг не может быть равен 0, смените его")

    def __iter__(self):
        self.pointer = self.start
        if self.is_step_valid():
            if self.step > 0:
                if self.is_count_up_valid():
                    return self
                else:
                    raise CountUpError("Начало отсчёта больше конца, при положительном шаге")
            if self.step < 0 and self.is_count_down_valid():
                return self
            else:
                raise CountDownError("Начало отсчёта меньше конца, при отрицательном шаге")
        else:
            raise StepValueError("Шаг не может быть равен 0, смените его")

    def __next__(self):
        self.pointer += self.step
        if self.step > 0 and self.pointer > self.stop + self.step:
            raise StopIteration
        elif self.step < 0 and self.pointer < self.stop + self.step:
            raise StopIteration
        else:
            return self.pointer - self.step

    def is_step_valid(self):
        if self.step != 0:
            return True
        else:
            return False

    def is_count_up_valid(self):
        if self.step > 0:
            if self.start < self.stop:
                return True
            else:
                return False

    def is_count_down_valid(self):
        if self.step < 0:
            if self.start > self.stop:
                return True
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    CoTeSt.colorful_text("Итератор 1:", CoTeSt.Color.CYAN)
    try:
        iter1 = Iterator(100, 200, 0)
        for i in iter1:
            print(i, end=' ')
    except StepValueError as exc:
        CoTeSt.colorful_text(exc.message, CoTeSt.Color.RED)
    iter2 = Iterator(-5, 1)
    iter3 = Iterator(6, 15, 2)
    iter4 = Iterator(5, 1, -1)
    iter5 = Iterator(10, 1)

    CoTeSt.colorful_text("\nИтератор 2:", CoTeSt.Color.CYAN)
    for i in iter2:
        print(i, end=' ')
    CoTeSt.colorful_text("\n\nИтератор 3:", CoTeSt.Color.CYAN)
    for i in iter3:
        print(i, end=' ')
    CoTeSt.colorful_text("\n\nИтератор 4:", CoTeSt.Color.CYAN)
    for i in iter4:
        print(i, end=' ')
    CoTeSt.colorful_text("\n\nИтератор 5:", CoTeSt.Color.CYAN)
    try:
        for i in iter5:
            print(i, end=' ')
    except CountUpError as exc:
        CoTeSt.colorful_text(exc.message, CoTeSt.Color.RED)
