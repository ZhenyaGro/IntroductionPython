# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например: positions = [1, 3, 6]).

from random import randint
from turtle import position


n = randint(3, 10)
array = []
j = -n
for i in range(0, n * 2 + 1):
    array.append(j)
    j += 1

print(array)


def multiply(array):
    positions = [1, 3, 6]
    return array[positions[0]] * array[positions[1]] * array[positions[2]]


print(multiply(array))
