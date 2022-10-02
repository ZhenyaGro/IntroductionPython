# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи] (https://ru.wikipedia.org/wiki/Негафибоначчи)

def fibonacci(n):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = 8
for i in range(number + 1):
    print(fibonacci(i))
