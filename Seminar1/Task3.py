# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def find_quarter():
    try:
        x = int(input('Введите x: '))
        y = int(input('Введите y: '))
    except:
        print('Некорректный ввод')
        return

    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x < 0 and y > 0:
        return 4
    else:
        return 0


result = find_quarter()
if result:
    print(result)
elif result == 0:
    print('Координаты: (0, 0)')
