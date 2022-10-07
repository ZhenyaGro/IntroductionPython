# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def create_polynomial():

    def random_number():
        return randint(0, 2)  # 101

    k = int(input('Введите k: '))
    result = []
    for i in range(-k, -1):
        current_number = random_number()
        if current_number == 1:
            result.append(f'x ** {-i}')
        elif current_number == 0:
            continue
        else:
            result.append(f'{current_number} * x ** {-i}')

    result.append(f'{random_number()} * x')
    result.append(f'{random_number()}')

    return result


print(create_polynomial())
