import numpy as np
import tkinter as tk
import os
import csv
import random
import math
import time
from modules import placestone, calcscore, calcresult, findinvalidinput, mytkinter
from modules import constant as const
from modules.qlearn import qagent
import copy

def osero_initialize(board):
    #0 = blank
    #1 = black
    #2 = white
    board[const.SIZE //2 - 1][const.SIZE // 2 - 1] = 2
    board[const.SIZE //2    ][const.SIZE // 2    ] = 2
    board[const.SIZE //2 - 1][const.SIZE // 2    ] = 1
    board[const.SIZE //2    ][const.SIZE // 2 - 1] = 1
    return board

def score_2dvec(board, color):
    score = [[0 for i in range(const.SIZE)] for j in range(const.SIZE)]
    for row in range(const.SIZE):
        for collumn in range(const.SIZE):
            if board[row][collumn] == 1 or board[row][collumn] == 2:
                score[row][collumn] -= 200000
            else:
                continue
    #print(score)
    for row in range(const.SIZE):
        for collumn in range(const.SIZE):
            if calcscore.score_count(board, row, collumn, color) > 0:
                score[row][collumn] += calcscore.score_count(board, row, collumn, color)
            else:
                score[row][collumn] -= 200000

    global turns
    for row in range(const.SIZE):
        for collumn in range(const.SIZE):
            score[row][collumn] += abs(int(random.gauss(0, 10))) // int(pow((turns+1), 0.5))
    
    return score
    

def cpu_placestone(board, color):
    global owaru1
    global owaru2
    bestscorex = -1
    bestscorey = -1
    bestscore = -1
    #score = score_calc2(board)
    #score = score_learning(board, const.WHITE)
    score = score_2dvec(board, color)

    for row in range(const.SIZE):
        for collumn in range(const.SIZE):
            if bestscore < score[row][collumn]:
                bestscore = score[row][collumn]
                bestscorex = row
                bestscorey = collumn
    if bestscorex >= 0:

        #print("cpu:"," ", bestscorex, ",", bestscorey)
        board = placestone.board_placestone(board, bestscorex, bestscorey, color)
        if color == 1:
            owaru1 = False
        elif color == 2:
            owaru2 = False
    else:
        #print("cpupass")
        global turns
        turns -= 1
        if color == 1:
            owaru1 = True
        elif color == 2:
            owaru2 = True

    return board

def score_qlearn(q, board, color):
    score = [[0 for i in range(const.SIZE)] for j in range(const.SIZE)]
    for row in range(const.SIZE):
        for collumn in range(const.SIZE):
            if board[row][collumn] == 1 or board[row][collumn] == 2:
                score[row][collumn] -= 2000000
            else:
                continue
    #print(score)
    for row in range(const.SIZE):
        for collumn in range(const.SIZE):
            if calcscore.score_count(board, row, collumn, color) > 0:
                state = q.board2state(board)
                score[row][collumn] += max(1, q.select_q(state, [row, collumn]))
            else:
                score[row][collumn] -= 2000000

    global turns
    #for row in range(const.SIZE):
        #for collumn in range(const.SIZE):
            #score[row][collumn] += abs(int(random.gauss(0, 10))) // int(pow((turns+1), 0.5))
    #print(score)
    return score
    
def cpu_placestone_qlearn(q, board, color):
    global turns, owaru1, owaru2
    global last_act_1, last_act_2, last_board_1, last_board_2

    bestscorex = -1
    bestscorey = -1
    bestscore = -1
    #score = score_calc2(board)
    #score = score_learning(board, const.WHITE)
    #score = score_2dvec(board, color)
    score = score_qlearn(q, board, color)
    #print(score)

    for row in range(const.SIZE):
        for collumn in range(const.SIZE):
            if bestscore < score[row][collumn]:
                bestscore = score[row][collumn]
                bestscorex = row
                bestscorey = collumn
    print(bestscore)  
    if bestscorex >= 0:
        #print("cpu:"," ", bestscorex, ",", bestscorey)
        cur_state = q.board2state(board)
        last_board = copy.deepcopy(board)
        board = placestone.board_placestone(board, bestscorex, bestscorey, color)
        if color == 1:
            owaru1 = False

            if turns != 0:
                #print(state, bestscorex, bestscorey)
                last_state = q.board2state(last_board_1)
                cur_best_score = q.select_q(cur_state, [bestscorex, bestscorey])  
                q.learning(last_state, last_act_1, cur_best_score)
            last_act_1 = [bestscorex, bestscorey]
            last_board_1 = last_board
            #print(last_board_1)
            

        elif color == 2:
            owaru2 = False

            if turns != 1:
                
                last_state = q.board2state(last_board_2)
                cur_best_score = q.select_q(cur_state, [bestscorex, bestscorey])      
                q.learning(last_state, last_act_2, cur_best_score)
            last_act_2 = [bestscorex, bestscorey]
            last_board_2 = last_board

    else:
        #print("cpupass")
        
        turns -= 1
        if color == 1:
            owaru1 = True
        elif color == 2:
            owaru2 = True

    return board

def player_placestone(board, row, collumn, color):
    global owaru1
    global owaru2
    global turns
    print(row, collumn)
    if (row >= const.SIZE or collumn >= const.SIZE or row < 0 or collumn < 0):
        print("playerpass(invalid input:out of space)")
        turns -= 1
        owaru1 = True
    else:
        if calcscore.score_count(board, row, collumn, color) < 1 or board[row][collumn] > 0:
            #if board[row][collumn]>0:
                #print("Yes")
            print("playerpass(invalid input:got no stones)")
            turns -= 1
            owaru1 = True
        else:
            board = placestone.board_placestone(board, row, collumn, color)
            owaru1 = False
    return board

def one_episode(tkgui):
    global turns, owaru1, owaru2
    global last_act_1, last_act_2, last_board_1, last_board_2
    turns = 0
    teban = 0
    owaru1 = False
    owaru2 = False
    #waittime = 0.000001
    waittime = 1
    board = [ [0] * const.SIZE for i in range(const.SIZE)]
    board = osero_initialize(board)
    tkgui.board_image(board)
    a = input("time control:")
    # for learning
    q1 = qagent.Qagent(const.DEFAULT_ALPHA, const.DEFAULT_GAMMA, const.BLACK)
    q2 = qagent.Qagent(const.DEFAULT_ALPHA, const.DEFAULT_GAMMA, const.WHITE)
    q1.load()
    q2.load()
   
    eps = const.DEFAULT_EPSILON

    last_act_1 = [-1, -1]
    last_act_2 = [-1, -1]
    last_board_1 = [[0 for i in range(const.SIZE)] for j in range(const.SIZE) ]
    last_board_1 = osero_initialize(last_board_1)
    last_board_2 = [[0 for i in range(const.SIZE)] for j in range(const.SIZE) ]
    last_board_2 = osero_initialize(last_board_2)

    while turns < const.SIZE**2 - 4:
        error = True
        #print(owaru1, owaru2)
        if owaru1 == False or owaru2 == False:

            #time.sleep(3)
            if teban // 2 * 2 + 1 == teban:
                while error:
                    try:
                        tkgui.wait_click(a)
                        board = player_placestone(board, tkgui.rowinput, tkgui.collumninput, const.WHITE)
                        
                        #board = cpu_placestone_black(board)
                        error = False
                        teban += 1
                        turns += 1
                        tkgui.board_image(board)

                    except ValueError:
                        print("error1 0~7 int please")
                        tkgui.board_image(board)
                #time.sleep(waittime)
                #board = cpu_placestone_qlearn(q1, board, const.BLACK)

            else:
                time.sleep(waittime)
                board = cpu_placestone_qlearn(q1, board, const.BLACK)
                teban += 1
                turns += 1
                tkgui.board_image(board)
                #board[row][collumn]
                time.sleep(waittime)
        else:
            break
    winner = calcresult.winner(board)
    print(winner)
    if winner[0] == "first player":
        q1.add_fee(q1.board2state(last_board_1), last_act_1, const.WINNER_SCORE)
        q2.add_fee(q2.board2state(last_board_2), last_act_2, const.LOSER_SCORE)

    elif winner[0] == "second player":
        q2.add_fee(q2.board2state(last_board_2), last_act_2, const.WINNER_SCORE)
        q1.add_fee(q1.board2state(last_board_1), last_act_1, const.LOSER_SCORE)
    
    #q1.save()
    #q2.save()
    tkgui.canvas.delete("all")

def main():
    tkgui = mytkinter.Tkgui()
    itr = 1
    for i in range(itr):
        one_episode(tkgui)
    
    return 0
    
main()