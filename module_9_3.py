first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) if len(x) > len(y) else len(y) - len(x)
                for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))

second_result = (len(x) == len(y) for x, y in zip(first, second))
print(list(second_result))
