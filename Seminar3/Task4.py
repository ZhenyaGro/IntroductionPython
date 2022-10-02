# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

users_number = int(input('Введите число: '))


def convert_to_bin(number):
    bin_number = ''
    while (number > 0):
        bin_number = str(number % 2) + bin_number
        number = number // 2

    return bin_number


print(convert_to_bin(users_number))
