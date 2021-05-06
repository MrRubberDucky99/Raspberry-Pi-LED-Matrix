# A Content file for Raspbery Pi LED Matrix
# Content Included, Basic X & Y Waves
# Made by Judah Fuller
# Started 6th March 2021

import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Setup import Matrix, columns, rows

def xWave ():
    x = 0

    while x < columns:
        Matrix.Set_Column_On(x)
        Matrix.output()
        time.sleep(0.15)
        Matrix.Set_Column_Off(x)
        x = x + 1
    Matrix.output()

def yWave ():
    x = 0

    while x < rows:
        Matrix.Set_Row_On(x)
        Matrix.output()
        time.sleep(0.15)
        Matrix.Set_Row_Off(x)
        x = x + 1
    Matrix.output()