from modules import constant as const

def winner(ban):
    first_player_score  = 0
    second_player_score = 0
    for gyou in range(const.SIZE):
        for retsu in range(const.SIZE):
            if ban[gyou][retsu] == const.BLACK:
                first_player_score += 1

    for gyou in range(const.SIZE):
        for retsu in range(const.SIZE):
            if ban[gyou][retsu] == const.WHITE:
                second_player_score += 1
                
    if first_player_score > second_player_score:
        winner = "first player"
    elif second_player_score > first_player_score:
        winner = "second player"
    else:
        winner = "DRAW"
    score = abs(first_player_score - second_player_score)
    return [winner, score]