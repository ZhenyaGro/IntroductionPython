# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

def find_sequence():
    sequence = []
    n = int(input('Введите n: '))

    if n == 0:
        print('0')
        return

    sum = 0
    for i in range(1, n + 1):
        current = round((1 + 1 / i) ** i, 2)
        sequence.append(current)
        sum += current

    print(sequence)
    return sum


print(find_sequence())
