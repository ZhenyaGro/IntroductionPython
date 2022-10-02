# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint, random
import random


def create_array():
    count_numbers = randint(5, 11)

    array = []
    for _ in range(0, count_numbers):
        array.append(round(random.uniform(0, 6), 2))

    return array


def find_min_max_difference(array):
    min = array[0] % 1
    max = array[0] % 1
    for i in range(1, len(array)):
        current_value = array[i] % 1
        if current_value > max:
            max = current_value
        elif current_value < min:
            min = current_value

    return round(max - min, 2)


array = create_array()
print(array)
print(find_min_max_difference(array))
