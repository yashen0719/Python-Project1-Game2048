import random

def initialize_game():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if not empty_cells:
        return board

    i, j = random.choice(empty_cells)
    board[i][j] = 2 if random.random() < 0.9 else 4
    return board

def move_left(board):
    new_board = []
    for row in board:
        new_row = [num for num in row if num != 0]
        new_row += [0] * (4 - len(new_row))
        for i in range(3):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [num for num in new_row if num != 0]
        new_row += [0] * (4 - len(new_row))
        new_board.append(new_row)
    return new_board

def move_right(board):
    new_board = [row[::-1] for row in board]
    new_board = move_left(new_board)
    new_board = [row[::-1] for row in new_board]
    return new_board

def move_up(board):
    board = [list(row) for row in zip(*board)]
    board = move_left(board)
    board = [list(row) for row in zip(*board)]
    return board

def move_down(board):
    board = [list(row) for row in zip(*board)]
    board = move_right(board)
    board = [list(row) for row in zip(*board)]
    return board

def check_game_over(board):
    for row in board:
        if 2048 in row:
            print("Congratulations! You reached 2048.")
            return True

    for row in board:
        if 0 in row:
            return False

    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1]:
                return False
            if board[j][i] == board[j + 1][i]:
                return False

    return True
