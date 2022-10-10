# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# File: 'Вася абв Приветабв Каабвк Тест'
# Result: 'Вася Тест'

# def read_file(path):
#     file = open(f'{path}', 'r')
#     return file.read().split()

def read_file(path):
    file = open(f'{path}', 'r')
    return [i for i in file.read().split() if i.find('абв') == -1]


print(read_file('Seminar5/FileTask1.txt'))
