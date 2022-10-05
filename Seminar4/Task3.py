# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


def create_array():
    array = []
    for _ in range(0, 6):
        array.append(randint(0, 10))

    return array


def find_unique(array):
    # return set(array)
    result = []
    for i in array:
        count = 0
        for j in array:
            if i == j:
                count += 1
        if count == 1:
            result.append(i)

    return result


some_array = create_array()
print(some_array)
print(find_unique(some_array))
