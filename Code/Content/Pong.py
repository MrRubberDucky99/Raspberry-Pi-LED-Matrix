# A Content file for Raspbery Pi LED Matrix
# Content Included: Pong
# Made by Judah Fuller

# Import Requirements
import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Setup import Matrix, columns, rows

class Paddle ():
    def __init__ (self, Matrix, Columns, Rows):
        self.Matrix = Matrix
        self.Columns = Columns
        self.Rows = Rows
        self.LEDs = Matrix.LEDs
        self.LEDNum = Matrix.LEDNum
    
    def Setup (self, posTop, posX):
        i = 0
        while i < self.LEDNum:
            x, y = Matrix.LEDs[i].getpos()
            if (x == posX) and (y <= (posTop+3) and y >= posTop):
                self.LEDs[i].On()
                self.LEDs[i].set_colour(0xFFFFFF)
            i = i + 1
        self.pos = [posTop, posTop+1, posTop+2, posTop+3]

class Game ():
    def __init__ (self, Matrix, Columns, Rows):
        self.Matrix = Matrix
        self.Columns = Columns
        self.Rows = Rows
        self.LEDs = Matrix.LEDs
        self.LEDNum = Matrix.LEDNum
        self.PaddleL = Paddle(self.Matrix, self.Columns, self.Rows)
        self.PaddleR = Paddle(self.Matrix, self.Columns, self.Rows)
    
    def DrawCenter (self):
        i = 0
        while i < self.LEDNum:
            x, y = Matrix.LEDs[i].getpos()
            if (x == ((columns)/2).__round__() or x == ((columns)/2).__round__()-1):
                    self.LEDs[i].On()
                    self.LEDs[i].set_colour(0xFFFFFF)
            i = 1 + 1

    def Reset (self):
        self.Matrix.Reset()
        self.PaddleL.Setup(4, 0)
        self.PaddleR.Setup(4, columns-1)
        self.DrawCenter
        self.Matrix.output()

Pong = Game(Matrix, columns, rows)
Pong.Reset()