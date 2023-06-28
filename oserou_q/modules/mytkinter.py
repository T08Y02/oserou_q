import tkinter as tk
from modules import constant as const

class Tkgui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(u"oserou")
        self.root.geometry("500x500")
        self.canvas = tk.Canvas(self.root, width = 500, height = 500)
        self.canvas.place(x=0, y=0)
        self.canvas.bind('<ButtonPress-1>', self.click_upload)
        self.clk_ok = True
        self.rowinput = 0
        self.collumninput = 0

    def board_image(self,board):
        self.canvas.delete("all")
        self.canvas.create_rectangle(50, 50, (const.SIZE+1) * 50, (const.SIZE+1) * 50, fill = 'green')
        for i in range(const.SIZE):
            self.canvas.create_line(50+50*i, 50, 50+50*i, (const.SIZE+1) * 50, fill='black', width = '1')
        for i in range(const.SIZE):
            self.canvas.create_line(50,50+50*i, (const.SIZE+1) * 50, 50+50*i, fill='black', width = '1')
        for i in range(const.SIZE):
            for j in range(const.SIZE):
                if board[i][j] == 1:
                    self.canvas.create_oval(50 + 50*j, 50 + 50*i, 100 + 50*j, 100 + 50*i, fill = 'black')
                elif board[i][j] == 2:
                    self.canvas.create_oval(50 + 50*j, 50 + 50*i, 100 + 50*j, 100 + 50*i, fill = 'white')
                else:
                    continue
        self.root.update()


    def click_upload(self, event):
        if self.clk_ok:
            self.canvas.delete('ovallll')
            self.rowinput = event.y // 50 - 1
            self.collumninput = event.x // 50 - 1
            self.canvas.delete('oval')
            self.canvas.create_oval(50 + 50*self.collumninput, 50 + 50*self.rowinput, 100 + 50*self.collumninput, 100 + 50*self.rowinput, fill = 'red', tag = 'oval')

    def clkok(self):
        self.clk_ok = False

    def wait_click(self, a):
        self.clk_ok = True
        self.canvas.create_oval(0, 0, 50, 50, fill = 'red', tag = 'ovallll')
        a = int(a)
        self.root.after(a * 1000, self.clkok)
        while self.clk_ok:
            self.root.update()