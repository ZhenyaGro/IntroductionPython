# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


def create_array():
    count_numbers = randint(5, 11)

    array = []
    for _ in range(0, count_numbers):
        array.append(randint(-9, 10))

    return array


def multiply_pairs(array):
    result = []

    for i in range(0, len(array) // 2):
        result.append(array[i] * array[-i - 1])

    if len(array) % 2 == 1:
        extra_element = array[len(array) // 2]
        result.append(extra_element ** 2)

    return result


array = create_array()
print(array)
print(multiply_pairs(array))
