import csv
from .. import constant as const
import os

class Qagent:
    #Q 学習機本体
    def __init__(self, alpha, gamma, color, initial_q=50.0):
        #Q 値、学習係数、伝播係数の設定
        self._values = {}
        self._alpha = alpha
        self._gamma = gamma
        self._initial_q = initial_q
        self.mycolor = color
        self.modelcsv = "./modules/qlearn/model/q_table_{0}.csv".format(self.mycolor)
        # with open(self.modelcsv, 'r') as f:
        #     reader = csv.reader(f)
        #     l = [row for row in reader]

        # print(l)
    
    def board2state(self, board):
        state = ""
        for i in range(const.SIZE):
            for j in range(const.SIZE):
                state += str(board[i][j])
        return int(state)

    def select_q(self, state, act):
        #状態とアクションをキーに、q 値取得
        if ((state, act[0], act[1])) in self._values.keys():
            #print("happy")
            return self._values[(state, act[0], act[1])]
        else:
            # Q 値が未学習の状況なら、Q 初期値
            # print(self._values.keys())
            self._values[(state, act[0], act[1])] = self._initial_q
            return self._initial_q

    def save(self):
        with open(self.modelcsv, 'w') as f:
            writer = csv.DictWriter(f, self._values.keys())
            writer.writeheader()
            writer.writerow(self._values)
            
    def load(self):
        with open(self.modelcsv) as f:
            reader = csv.DictReader(f)
            for row in reader:
                for key, value in row.items():
                    tpl_key = eval(key)
                    self._values[tpl_key] = float(value)
        # for key, value in self._values.items():
        #     print(type(value))


    def set(self, state, act, q_value):
        #Q 値設定
        self._values[(state, act[0], act[1])] = q_value

    def learning(self, state, act, max_q):
        #Q 値更新
        #print("happy")
        pQ = self.select_q(state, act)
        new_q = pQ + self._alpha * (self._gamma * (max_q - pQ))
        #print(new_q - pQ)
        self.set(state, act, new_q)

    def add_fee(self, state, act, fee):
        #報酬を与える
        pQ = self.select_q(state, act)
        new_q = pQ + self._alpha * (fee - pQ)
        self.set(state, act, new_q)