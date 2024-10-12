def is_prime(func):
    def wrapper(first, second, third):
        result = first + second + third
        for digit in range(2, result//2):
            if result % digit == 0:
                print("Составное")
                break
        else:
            print("Простое")
        return result
    return wrapper


@is_prime
def sum_three(first, second, third):
    return first + second + third


print(sum_three(1, 2, 4))
print(sum_three(2, 3, 6))
print(sum_three(123, 4, 123))
print(sum_three(1, 1, 1))
