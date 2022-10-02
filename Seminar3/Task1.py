# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


def create_array():
    count_numbers = randint(5, 10)

    array = []
    for _ in range(0, count_numbers):
        array.append(randint(-9, 10))

    return array


def calculate_odd_positions(array):
    sum = 0
    for i in range(1, len(array), 2):
        sum += array[i]

    return sum


array = create_array()
print(array)
print(calculate_odd_positions(array))
