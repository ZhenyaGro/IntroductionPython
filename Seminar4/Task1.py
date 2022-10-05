# Вычислить число c заданной точностью d
# *Пример:*
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math


def round_number(number):
    d = input('Введите точность в формате "0.001": ')
    accuracy = d.split('.')
    return round(number, len(accuracy[1]))


print(round_number(math.pi))
