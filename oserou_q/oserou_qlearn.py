import numpy as np
import tkinter as tk
import os
import csv
import random
import math
import time
from modules import placestone, calcscore, calcresult, findinvalidinput, mytkinter
from modules import constant as const

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
    

def cpu_placestone_white(board):
    global owaru1
    global owaru2
    bestscorex = -1
    bestscorey = -1
    bestscore = -1
    #score = score_calc2(board)
    #score = score_learning(board, const.WHITE)
    score = score_2dvec(board, const.WHITE)

    for row in range(const.SIZE):
        for collumn in range(const.SIZE):
            if bestscore < score[row][collumn]:
                bestscore = score[row][collumn]
                bestscorex = row
                bestscorey = collumn
    if bestscorex >= 0:

        #print("cpu:"," ", bestscorex, ",", bestscorey)
        board = placestone.board_placestone(board, bestscorex, bestscorey, const.WHITE)
        owaru2 = False
    else:
        print("cpupass")
        global turns
        turns -= 1
        #global owaru2
        owaru2 = True
    return board

def cpu_placestone_black(board):
    global owaru1
    global owaru2
    bestscorex = -1
    bestscorey = -1
    bestscore = -1
    #score = score_calc2(board)
    #score = score_learning(board, const.WHITE)
    score = score_2dvec(board, const.BLACK)

    for row in range(const.SIZE):
        for collumn in range(const.SIZE):
            if bestscore < score[row][collumn]:
                bestscore = score[row][collumn]
                bestscorex = row
                bestscorey = collumn
    if bestscorex >= 0:
        #print("cpu:"," ", bestscorex, ",", bestscorey)
        board = placestone.board_placestone(board, bestscorex, bestscorey, const.BLACK)
        owaru1 = False
    else:
        print("cpu1pass")
        global turns
        turns -= 1
        #global owaru2
        owaru1 = True
    return board

def player_placestone(board, row, collumn):
    global owaru1
    global owaru2
    global turns
    print(row, collumn)
    if (row >= const.SIZE or collumn >= const.SIZE or row < 0 or collumn < 0):
        print("playerpass(invalid input:out of space)")
        turns -= 1
        owaru1 = True
    else:
        if calcscore.score_count(board, row, collumn, 1) < 1 or board[row][collumn] > 0:
            #if board[row][collumn]>0:
                #print("Yes")
            print("playerpass(invalid input:got no stones)")
            turns -= 1
            owaru1 = True
        else:
            board = placestone.board_placestone(board, row, collumn, 1)
            owaru1 = False
    return board

def one_episode():


def main():
    tkgui = mytkinter.Tkgui()
    global turns, owaru1, owaru2
    turns = 0
    teban = 0
    owaru1 = False
    owaru2 = False
    board = [ [0] * const.SIZE for i in range(const.SIZE)]
    board = osero_initialize(board)
    tkgui.board_image(board)
    a = input("time control:")

    while turns < const.SIZE**2 - 4:
        error = True
        print(owaru1, owaru2)
        if owaru1 == False or owaru2 == False:

            #time.sleep(3)
            if teban // 2 * 2 == teban:
                # while error:
                #     try:
                #         tkgui.wait_click(a)
                #         board = player_placestone(board, tkgui.rowinput, tkgui.collumninput)
                #         board = cpu_placestone_black(board)
                #         error = False
                #         teban += 1
                #         turns += 1
                #         tkgui.board_image(board)

                #     except ValueError:
                #         print("error1 0~7 int please")
                #         tkgui.board_image(board)
                time.sleep(3)
                board = cpu_placestone_black(board)
                #error = False
                teban += 1
                turns += 1
                tkgui.board_image(board)

            else:
                time.sleep(3)
                board = cpu_placestone_white(board)
                teban += 1
                turns += 1
                tkgui.board_image(board)
        else:
            break

    #board[row][collumn]
    time.sleep(3)
    print(calcresult.winner(board))
    teban = 0

    tkgui.board_image(board)
    return 0
    
main()