# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def check_weekday(day):
    if day < 1 or day > 7:
        return 'Некорректный ввод'
    elif day < 7 and day > 5:
        return 'Да (выходной)'
    else:
        return 'Нет (будний)'


try:
    weekday = int(input('Введите день недели: '))
    print(check_weekday(weekday))
except:
    print('Некорректный ввод')
