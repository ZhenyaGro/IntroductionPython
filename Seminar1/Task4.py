# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def find_coodrinates():
    try:
        quarter = int(input('Введите номер четверти: '))
    except:
        print('Некорректный ввод')
        return

    if quarter == 1:
        return '(0, 0) -> (∞; ∞)'
    elif quarter == 2:
        return '(0, 0) -> (∞; -∞)'
    elif quarter == 3:
        return '(0, 0) -> (-∞; -∞)'
    elif quarter == 4:
        return '(0, 0) -> (-∞; ∞)'
    else:
        return 'Некорректный номер четверти'


print(find_coodrinates())
