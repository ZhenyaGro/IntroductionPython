# Создайте программу для игры с конфетами человек против человека.¡
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


def choose_mode():
    game_mode = input(
        'Выбор режима игры.\n1 - Против игрока\n2 - Против бота\nРежим: ')
    if game_mode != '1' and game_mode != '2':
        print('Выбран некорректный режим')

    return game_mode


count_candy = 120


def pvp(candy):
    print(f'Количество конфет: {candy}')
    current_player = randint(1, 2)
    print(f'Первым ходит: Игрок {current_player}')
    if current_player == 1:
        first_player = True
    else:
        first_player = False

    can_get = 28
    while candy != 0:
        if first_player == True:
            current_player = 1
        elif first_player == False:
            current_player = 2

        print(
            f'\nХод Игрока {current_player}\nТекущее количество конфет: {candy}')

        if candy < 28:
            can_get = candy

        try:
            take_candy = int(input(f'Заберите от 1 до {can_get} конфет: '))
        except:
            take_candy = 29
        while take_candy < 1 or take_candy > can_get:
            print('Некорректное количество конфет. Попробуйте еще раз')
            try:
                take_candy = int(
                    input(f'Заберите от 1 до {can_get} конфет: '))
            except:
                take_candy = 29

        candy -= take_candy
        first_player = not first_player

    print(f'\nВыиграл Игрок {current_player}')

    return


def pve(candy):
    return


game_mode = choose_mode()
if game_mode == '1':
    pvp(count_candy)
if (game_mode == '2'):
    pve(count_candy)
