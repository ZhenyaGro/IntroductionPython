# Создайте программу для игры с конфетами человек против человека.¡
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint
import time


def choose_mode():
    game_mode = input(
        'Выбор режима игры.\n1 - Против игрока 👥\n2 - Против Компьютера 🤖\nРежим: ')
    if game_mode != '1' and game_mode != '2':
        print('Выбран некорректный режим. Запущена игра против Компьютера 🤖')
        return '2'

    return game_mode


count_candy = 120


def game(mode, candy):

    def show_player(mode, current_player, is_first_move=False):
        if is_first_move:
            if mode == '2' and current_player == 2:
                print(f'Первым ходит: Компьютер 🤖')
                return 2
            else:
                print(f'Первым ходит: Игрок {current_player}')
        else:
            if mode == '2' and current_player == 2:
                print(
                    f'\nХодит Компьютер 🤖\nТекущее количество конфет: {candy} 🍬')
                return 2
            else:
                print(
                    f'\nХодит Игрок {current_player}\nТекущее количество конфет: {candy} 🍬')

    print(f'Начальное количество конфет: {candy} 🍬')
    current_player = randint(1, 2)
    show_player(mode, current_player, True)

    is_first_player = True if current_player == 1 else False

    def make_move(current_candy, can_get):
        if current_candy < 28:
            can_get = current_candy

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

        return take_candy

    def bot_move(candy, can_get):
        time.sleep(1)
        if candy == can_get:
            print(f'Компьютер забрал {candy} 🍬')
            return candy
        bot_take = candy % (can_get + 1)
        if bot_take != 0:
            print(f'Компьютер забрал {bot_take} 🍬')
            return bot_take
        else:
            bot_take = randint(1, can_get)
            print(f'Компьютер забрал {bot_take} 🍬')
            return bot_take

    max_get = 28
    while candy != 0:
        current_player = 1 if is_first_player == True else 2
        show_player(mode, current_player)
        if mode == '1':
            candy -= make_move(candy, max_get)
        if mode == '2':
            if current_player == 1:
                candy -= make_move(candy, max_get)
            if current_player == 2:
                candy -= bot_move(candy, max_get)

        is_first_player = not is_first_player

    if mode == '2' and is_first_player:
        print(f'\nВыиграл Компьютер! Все конфеты принадлежат ему! 🍬 🤖 🍬🍬')
        print(
            '\n🤖: Сначала эти конфеты, а затем и весь мир! Ха-ха ха-ха\n(Роботский смех)\n')
    else:
        print(f'\nВыиграл Игрок {current_player}! Все конфеты Ваши! 🍬 🙂 🍬🍬')

    return


game_mode = choose_mode()
game(game_mode, count_candy)
