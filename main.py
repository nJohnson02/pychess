import os
import sys
from tkinter import *

sys.path.insert(0, 'src')
from src import movement, pieces
from config import config

win = Tk()

# Setup
win.wm_iconbitmap('assets/blackKnight.ico')
win.wm_title('Chess')

class Board:

    def __init__(self, win):

        self.coords = []

        boardFrame = Frame(win)
        boardFrame.grid()

        blank = PhotoImage(file='assets/pieces/blank.png')

        for r in range(8):

            for c in range(8):

                btn = Button(boardFrame, image=blank, width=75, height=75, borderwidth=0)
                btn.configure(background='#fff')
                btn.image = blank

                if ((r % 2 == 0) & (c % 2 == 0)) | (r % 2 == c % 2):
                    btn.configure(background=config.boardCol)

                btn.grid(row=r, column=c)

                self.coords.append(pieces.Coordinate((r, c), btn, blank))

    def setBoard(self):
        
        pass

board = Board(win)

win.mainloop()

