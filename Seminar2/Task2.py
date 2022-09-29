# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

users_number = int(input('Введите число N: '))


def multiply_numbers(number):
    if number > 0:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

    if number < 0:
        result = -1
        for i in range(number, 0):
            result *= i
        return result

    if number == 0:
        return 0


print(multiply_numbers(users_number))
