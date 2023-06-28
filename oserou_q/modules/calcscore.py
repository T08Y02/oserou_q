from modules import constant as const

def score_count(board, gyou, retsu, color):
    if color == const.WHITE:
        before_c = const.BLACK
        after_c = const.WHITE
    else:
        before_c = const.WHITE
        after_c = const.BLACK

    ue = 0
    migiue = 0
    migi = 0
    migisita = 0
    sita = 0
    hidarisita = 0
    hidari = 0
    hidariue = 0
    scoreall = 0

    for i in range(gyou+1):
        if i == 0:
            if gyou-i == 0:
                break
            else:
                continue
        else:
            if gyou - i == 0:
                if board[gyou-i][retsu] == after_c:
                    break
                else:
                    ue = 0
                    break
            else:
                if board[gyou-i][retsu] == before_c:
                    ue += 1
                elif board[gyou-i][retsu] == after_c:
                #print(gyou-i)
                    break
                else:
                    ue = 0
                    break

    for i in range(const.SIZE - retsu):
        if i==0:
            if retsu + i == (const.SIZE - 1):
                break
            else:
                continue
        else:
            if retsu + i == (const.SIZE - 1):
                if board[gyou][retsu + i] == after_c:
                    break
                else:
                    migi = 0
                    break
            else:
                if board[gyou][retsu + i] == before_c:
                    migi += 1
                elif board[gyou][retsu + i] == after_c:
                    break
                else:
                    migi = 0
                    break

    for i in range(const.SIZE - gyou):
        if i==0:
            if gyou + i == (const.SIZE - 1):
                break
            else:
                continue
        else:
            if gyou + i == (const.SIZE - 1):
                if board[gyou+i][retsu] == after_c:
                    break
                else:
                    sita = 0
                    break
            else:
                if board[gyou+i][retsu] == before_c:
                    sita += 1
                elif board[gyou + i][retsu] == after_c:
                    break
                else:
                    sita = 0
                    break


    for i in range(retsu+1):
        if i == 0:
            if retsu - i == 0:
                break
            else:
                continue
        else:
            if retsu - i == 0:
                if board[gyou][retsu - i] == after_c:
                    break
                else:
                    hidari = 0
                    break
            else:
                if board[gyou][retsu-i] == before_c:
                    hidari += 1
                elif board[gyou][retsu-i] == after_c:
                    #print(gyou-i)
                    break
                else:
                    hidari = 0
                    break


    for i in range(gyou+1):
        if i==0:
            if retsu + i == (const.SIZE - 1) or gyou - i == 0:
                break
            else:
                continue
        else:
            if retsu + i == (const.SIZE - 1):
                if board[gyou - i][retsu + i] == after_c:
                    break
                else:
                    migiue = 0
                    break
            elif gyou - i == 0:
                if board[gyou - i][retsu + i] == after_c:
                    break
                else:
                    migiue = 0
                    break
            else:
                if board[gyou - i][retsu + i] == before_c:
                    migiue += 1
                elif board[gyou - i][retsu + i] == after_c:
                    break
                else:
                    migiue = 0
                    break


    for i in range(const.SIZE - gyou):
        if i==0:
            if retsu + i == (const.SIZE - 1) or gyou + i == (const.SIZE - 1):
                break
            else:
                continue
        else:
            if retsu + i == (const.SIZE - 1):
                if board[gyou + i][retsu + i] == after_c:
                    break
                else:
                    migisita = 0
                    break
            elif gyou + i == (const.SIZE - 1):
                if board[gyou + i][retsu + i] == after_c:
                    break
                else:
                    migisita = 0
                    break
            else:
                if board[gyou + i][retsu + i] == before_c:
                    migisita += 1
                elif board[gyou + i][retsu + i] == after_c:
                    break
                else:
                    migisita = 0
                    break



    for i in range(const.SIZE- gyou):
        if i==0:
            if retsu - i == 0 or gyou + i == (const.SIZE - 1):
                break
            else:
                continue
        else:
            if retsu - i == 0:
                if board[gyou + i][retsu - i] == after_c:
                    break
                else:
                    hidarisita = 0
                    break
            elif gyou + i == (const.SIZE - 1):
                if board[gyou + i][retsu - i] == after_c:
                    break
                else:
                    hidarisita = 0
                    break
            else:
                if board[gyou + i][retsu - i] == before_c:
                    hidarisita += 1
                elif board[gyou + i][retsu - i] == after_c:
                    break
                else:
                    hidarisita = 0
                    break



    for i in range(gyou+1):
        if i==0:
            if retsu - i == 0 or gyou - i == 0:
                break
            else:
                continue
        else:
            if retsu - i == 0:
                if board[gyou - i][retsu - i] == after_c:
                    break
                else:
                    hidariue = 0
                    break
            elif gyou - i == 0:
                if board[gyou - i][retsu - i] == after_c:
                    break
                else:
                    hidariue = 0
                    break
            else:
                if board[gyou - i][retsu - i] == before_c:
                    hidariue += 1
                elif board[gyou - i][retsu - i] == after_c:
                    break
                else:
                    hidariue = 0
                    break

    scoreall = ue + migiue + migi + migisita + sita + hidarisita + hidari + hidariue
    return scoreall