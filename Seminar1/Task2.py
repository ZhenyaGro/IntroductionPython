# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x, y, z = [0, 1], [0, 1], [0, 1]

x, y, z = [0, 1], [0, 1], [0, 1]


def check_true(x, y, z):
    for i in x:
        for j in y:
            for m in z:
                if not (x or y or z) != (not x and not y and not z):
                    return 0
    return 1


if check_true(x, y, z):
    print('Истина')
else:
    print('Ложь')
