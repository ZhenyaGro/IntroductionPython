# Реализовать алгоритм перемешивания списка.

from array import array
from random import randint


def create_array():
    array = []
    for i in range(0, 10):
        array.append(randint(-9, 10))
    return array


def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


arr = create_array()
print(arr)
print(bubble_sort(arr))
