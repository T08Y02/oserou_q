from modules import placestone, calcscore
from modules import constant as const

def bestScore(board_state, color):
    bestscore = 0
    for i in range(const.SIZE):
        for j in range(const.SIZE):
            if board_state[i][j] == 0:
                bestscore = max([bestscore, calcscore.score_count(board_state, i, j, color)])
    return bestscore

def checkValid(board_state, selected_row, selected_collumn, color):
    valid = 0

    bestscore = bestScore(board_state, color)
    if board_state[selected_row][selected_collumn] != 0 or \
        calcscore.score_count(board_state, selected_row, selected_collumn, color) <= 0:
        if bestscore <= 0:
            if calcscore.score_count(board_state, selected_row, selected_collumn, color % 2 + 1) <= 0:
                valid = 3
            else:
                valid = 2
        else:
            valid = 1
    return valid
    
