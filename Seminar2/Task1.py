# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

users_number = input('Введите число: ').replace('.', '')

sum = 0
for digit in users_number:
    sum += int(digit)

print(sum)
