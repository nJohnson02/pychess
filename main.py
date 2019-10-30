
import os
import sys
from tkinter import *

print("Running TKinter version", TkVersion)

sys.path.insert(0, 'src')
from src import movement, pieces
from config import config

win = Tk()

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

                pos = 8 * r + c 
                # Updates by the time btnClick(pos) is called; resulting in 63 not the desired result.
                
                btn = Button(boardFrame, image=blank, width=75, height=75, borderwidth=0, command=lambda:self.btnClick(pos))
                btn.configure(background='#fff')
                btn.image = blank

                if ((r % 2 == 0) & (c % 2 == 0)) | (r % 2 == c % 2):
                    btn.configure(background=config.boardCol)

                btn.grid(row=r, column=c)

                self.coords.append(pieces.Coordinate((r, c), btn, blank))

    def btnClick(self, pos):

        blank = PhotoImage(file='assets/pieces/blank.png')
        self.coords[pos].label.configure(image=blank)
        self.coords[pos].label.image = blank

        # Rather than removing the image, set the background color to a shade of a color.

    def setBoard(self):
    
        for piece in config.pieces:
            
            for coord in range(len(config.pieces[piece])):

                newImg = PhotoImage(file='assets/pieces/' + piece)
                pos = 8 * (config.pieces[piece][coord][0]) + config.pieces[piece][coord][1]

                self.coords[pos].label.configure(image=newImg)
                self.coords[pos].label.image = newImg

board = Board(win)
board.setBoard()
# setBoard() should eventually be called only when a game starts

win.mainloop()

