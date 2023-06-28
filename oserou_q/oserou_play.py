import numpy as np
import tkinter as tk
import os
import csv
import random
import math
import time
from modules import placestone, calcscore, calcresult, findinvalidinput, mytkinter
from modules import constant as const

def osero_initialize(ban):
    #0 = blank
    #1 = black
    #2 = white
    ban[3][3] = 2
    ban[4][4] = 2
    ban[3][4] = 1
    ban[4][3] = 1
    return ban

def score_2dvec(ban):
    score = [[0 for i in range(const.SIZE)] for j in range(const.SIZE)]
    for gyou in range(const.SIZE):
        for retsu in range(const.SIZE):
            if ban[gyou][retsu] == 1 or ban[gyou][retsu] == 2:
                score[gyou][retsu] -= 200000
            else:
                continue

    for gyou in range(const.SIZE):
        for retsu in range(const.SIZE):
            if calcscore.score_count(ban, gyou, retsu, 2) > 0:
                score[gyou][retsu] += calcscore.score_count(ban, gyou, retsu, 2)
            else:
                score[gyou][retsu] -= 200000

    global turns
    for gyou in range(const.SIZE):
        for retsu in range(const.SIZE):
            score[gyou][retsu] += abs(int(random.gauss(0, 10))) // int(pow((turns+1), 0.5))

    return score

def cpu_placestone(ban):
    global owaru1
    global owaru2
    bestscorex = -1
    bestscorey = -1
    bestscore = -1
    #score = score_calc2(ban)
    #score = score_learning(ban, const.WHITE)
    score = score_2dvec(ban)

    for gyou in range(8):
        for retsu in range(8):
            if bestscore < score[gyou][retsu]:
                bestscore = score[gyou][retsu]
                bestscorex = gyou
                bestscorey = retsu
    if bestscorex >= 0:

        #print("cpu:"," ", bestscorex, ",", bestscorey)
        ban = placestone.board_placestone(ban, bestscorex, bestscorey, 2)
        owaru1 = False
        owaru2 = False
    else:
        print("cpupass")
        global turns
        turns -= 1
        #global owaru2
        owaru2 = True
    return ban

def player_placestone(ban, gyou, retsu):
    global owaru1
    global owaru2
    print(gyou, ",", retsu)
    if calcscore.score_count(ban, gyou, retsu, 1) < 1 or ban[gyou][retsu] > 0:
        #if ban[gyou][retsu]>0:
            #print("Yes")
        print("playerpass")
        global turns
        turns -= 1
        owaru1 = True
    else:
        ban = placestone.board_placestone(ban, gyou, retsu, 1)
        owaru1 = False
        owaru2 = False
    return ban

def main():
    tkgui = mytkinter.Tkgui()
    global turns
    turns = 0
    teban = 0
    gyoudayo = 0
    retudayo = 0
    owaru1 = False
    owaru2 = False
    ban = [ [0] * 8 for i in range(8)]
    ban = osero_initialize(ban)
    tkgui.ban_image(ban)
    a = input("time control:")

    while turns < 60:
        error = True
        if owaru1 == False or owaru2 == False:

            #time.sleep(3)
            if teban // 2 * 2 == teban:
                while error:
                    try:
                        tkgui.wait_click(a)
                        ban = player_placestone(ban, gyoudayo, retudayo)
                        error = False
                        teban += 1
                        turns += 1
                        tkgui.ban_image(ban)

                    except ValueError:
                        print("error1 0~7 int please")
                        tkgui.ban_image(ban)

            else:
                time.sleep(3)
                ban = cpu_placestone(ban)
                teban += 1
                turns += 1
                tkgui.ban_image(ban)
        else:
            break

    #ban[gyou][retsu]
    time.sleep(3)
    print(calcresult.winner(ban))
    teban = 0

    tkgui.ban_image(ban)
    return 0
    
main()