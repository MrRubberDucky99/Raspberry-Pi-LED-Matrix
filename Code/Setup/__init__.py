# Setup file for Raspbery Pi LED Matrix
# Made by Judah Fuller

# Import Requirements
import LED.Sim as LEDSim

# Declare Global Vars
simOn = True
rows = 12
columns = 32

# Setup for simulated LEDs
if simOn == True:

    # Iteration Vars
    x = 0
    y = 0

    # Declare Create Simulated LED Positions
    LEDposX = []
    LEDposY = []
    while x < columns:
        LEDposX.append(x)
        x = x + 1
    LEDposX = LEDposX * rows
    while y < rows:
        LEDposY = LEDposY + ([y] * columns)
        y = y + 1

    #Set the matrix to the simulated one
    Matrix = LEDSim.MatrixSim(columns, rows, LEDposX, LEDposY)
    
else:
    Matrix = False