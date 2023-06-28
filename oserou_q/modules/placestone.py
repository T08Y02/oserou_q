from modules import constant as const

def board_place(board, gyou, retsu, color):
    board[gyou][retsu] = color
    return board

def board_reverse(board, gyou, retsu):
    if board[gyou][retsu] == const.BLACK:
        board[gyou][retsu] = const.WHITE
    elif board[gyou][retsu] == const.WHITE:
        board[gyou][retsu] = const.BLACK
    else:
        print("error")
    return board

def board_reverse_onestone(board, gyou, retsu, color):
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
    for i in range(ue):
        board = board_reverse(board, gyou - i - 1, retsu)

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
    for i in range(migi):
        board = board_reverse(board, gyou, retsu + i + 1)

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
    for i in range(sita):
        board = board_reverse(board, gyou + i + 1, retsu)


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

    for i in range(hidari):
        board = board_reverse(board, gyou, retsu - i - 1)

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
    for i in range(migiue):
        board = board_reverse(board, gyou - i - 1, retsu + i + 1)


    for i in range(const.SIZE- gyou):
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
    for i in range(migisita):
        board = board_reverse(board, gyou + i + 1, retsu + i + 1)


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
    for i in range(hidarisita):
        board = board_reverse(board, gyou + i + 1, retsu - i - 1)


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
    for i in range(hidariue):
        board = board_reverse(board, gyou - i - 1, retsu - i - 1)
    return board

def board_placestone(board, gyou, retsu, color):
    board = board_place(board, gyou, retsu, color)
    board = board_reverse_onestone(board, gyou, retsu, color)
    return board
