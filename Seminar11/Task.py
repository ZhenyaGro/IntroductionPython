# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

from sympy import *
import matplotlib.pyplot as plt
import math
import numpy

# 1. Определить корни


def f(x):
    return -12 * x ** 4 * numpy.sin(
        numpy.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30


# 4. Построить график
def graph():
    x = [x for x in range(-30, 30)]
    y = [(-12 * x ** 4 * math.sin(math.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30) for
         x in range(-30, 30)]
    plt.plot(x, y)
    plt.grid()
    plt.show()


print('Функция: f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30')
print(f(1))
