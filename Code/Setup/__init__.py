from LEDSim import LEDSim

# Declare Global Vars
simOn = True
rows = 12
columns = 32

# Setup for simulated LEDs
if simOn == True:

    # Iteration Vars
    x = 0
    y = 0

    # Declare LEDs
    LEDposX = []
    LEDposY = []
    while x < columns:
        LEDposX.append(x)
        x = x + 1
    LEDposX = LEDposX * rows
    while y < rows:
        LEDposY = LEDposY + ([str(y)] * columns)
        y = y + 1


    def MatrixSetup ():
        return LEDSim.MatrixSim(columns, rows, LEDposX, LEDposY)
    
else:
    def MatrixSetup ():
        return False

Matrix = MatrixSetup()