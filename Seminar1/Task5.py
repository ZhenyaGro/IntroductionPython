# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


def calculate_distance():
    print('Координаты точки A')
    try:
        a_x = int(input('Введите координату x точки A: '))
        a_y = int(input('Введите координату y точки A: '))
    except:
        return 'Некорректный ввод'

    print('Координаты точки B')
    try:
        b_x = int(input('Введите координату x точки B: '))
        b_y = int(input('Введите координату y точки B: '))
    except:
        return 'Некорректный ввод'

    return math.sqrt((b_x - a_x) ** 2 + (b_y - a_y) ** 2)


print('{:.2f}'.format(calculate_distance()))
