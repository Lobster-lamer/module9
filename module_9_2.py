first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(first_str) for first_str in first_strings if len(first_str) > 5]
print(first_result)

second_result = [(from_first, from_second) for from_first in first_strings for from_second in second_strings
                 if len(from_first) == len(from_second)]
print(second_result)

third_result = [{first_str: len(first_str)} for first_str in first_strings + second_strings if not len(first_str) % 2]
print(third_result)
