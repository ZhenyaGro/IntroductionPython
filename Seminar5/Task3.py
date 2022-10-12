# Создайте программу для игры в "Крестики-нолики".

def game():

    def create_game():
        return ['_' for i in range(9)]

    def show_board(board):
        print('')
        print(f'[{board[0]}, {board[1]}, {board[2]}]')
        print(f'[{board[3]}, {board[4]}, {board[5]}]')
        print(f'[{board[6]}, {board[7]}, {board[8]}]')
        print('')

    def make_move(board, player):
        print(f'Ходит {player}')
        try:
            move = int(input('Выберите поле для хода (1 - 9): ')) - 1
        except:
            print('Некорректный номер поля')
            return False
        if move < 0 or move > 8:
            print('Некорректный номер поля')
            return False

        if board[move] != '_':
            print('Поле уже заполнено')
            return False
        board[move] = player
        player_positions[player].append(move)

        return True

    def check_victory(player_positions, current_player):
        win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
            0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for i in win_combinations:
            if all(j in player_positions[current_player] for j in i):
                return True
        return False

    def check_endgame(player_positions):
        if len(player_positions['X']) + len(player_positions['O']) == 9:
            return True
        return False

    game_board = create_game()
    current_player = 'X'
    player_positions = {'X': [], 'O': []}
    show_board(game_board)

    while True:
        move_success = False
        while not move_success:
            move_success = make_move(game_board, current_player)
            show_board(game_board)
            if move_success:

                if check_victory(player_positions, current_player):
                    print(f'Победил {current_player}')
                    return current_player

                if check_endgame(player_positions):
                    print('Ничья')
                    return current_player

                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'


game()
