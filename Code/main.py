# Main file for Raspbery Pi LED Matrix
# Made by Judah Fuller
# Started 6th March 2021

# Import Requirements
import time, LEDSim, LEDLive

# Declare Global Vars
simOn = True

# Setup for simulated LEDs
if simOn == True:

    # Iteration Vars
    x = 0
    y = 0

    # Declare LEDs
    rows = 12
    columns = 32
    LEDposX = []
    LEDposY = []
    while x < columns:
        LEDposX.append(x)
        x = x + 1
    LEDposX = LEDposX * rows
    while y < rows:
        LEDposY = LEDposY + ([str(y)] * columns)
        y = y + 1


    def Matrix ():
        return sim.MatrixSim(32, 12, LEDposX, LEDposY)

else:
    Matrix = 0

Matrix.output()
time.sleep(5)
Matrix.Set_Row_On(2)
Matrix.Set_Row_On(9)
Matrix.Set_Column_On(2)
Matrix.Set_Column_On(29)
Matrix.output()