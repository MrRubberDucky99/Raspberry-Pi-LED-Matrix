# Main file for Raspbery Pi LED Matrix
# Made by Judah Fuller
# Started 6th March 2021

# Import Requirements
import time, Setup
from Content.Wave import xWave, yWave
from Content.Pong import Game
from Setup import Matrix, columns, rows

Matrix.Reset()

# Run Wave across X axis then Y Axis
xWave()
yWave()

time.sleep(2.5)

Pong = Game(Matrix, columns, rows)
Pong.Setup()