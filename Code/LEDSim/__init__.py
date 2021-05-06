# Simulated LED file for Raspbery Pi LED Matrix
# Made by Judah Fuller

# Import Requirements
from datetime import datetime

# Declare Class for Simulating LEDs
class LEDSim ():

    def __init__ (self, posX, posY):
        self.on = False
        self.x = posX
        self.y = posY

    def On (self):
        self.on = True
    
    def Off (self):
        self.on = False

    def getX (self):
        return self.x

#Declare Class for Simulating Matrix
class MatrixSim ():

    # Inital Setup
    def __init__ (self, LEDColumns, LEDRows, LEDPosX, LEDPosY):
        self.LEDNum = LEDColumns * LEDRows
        self.LEDColumns = LEDColumns
        self.LEDRows = LEDRows
        self.LEDs = []
        x = 0
        while x < self.LEDNum:
            # print(x)
            self.LEDs.append(LEDSim(LEDPosX[x], LEDPosY[x]))
            x = x + 1
    
    # Prepare and return text output for sim
    def output (self):
        y = 0
        x = 0
        i = 0
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        outStr = "\n Time: " + str(current_time) + "\n \n"
        while x < self.LEDRows:
            while i < self.LEDColumns:
                if self.LEDs[y].on == True: outStr = outStr + " 1"
                else: outStr = outStr + " 0"
                i = i + 1
                y = y + 1
            x = x + 1
            i = 0
            outStr = outStr + "\n"
        print(outStr)

    def Set_Row_On (self, row):
        x = self.LEDColumns * row
        while x < (self.LEDColumns * (row + 1)):
            self.LEDs[x].On()
            x = x + 1

    def Set_Column_On (self, column):
        x = 0
        while x < self.LEDNum:
            LEDx = self.LEDs[x].getX()
            if LEDx == column:
                self.LEDs[x].On()
            x = x + 1
    
    def Set_Row_Off (self, row):
        x = self.LEDColumns * row
        while x < (self.LEDColumns * (row + 1)):
            self.LEDs[x].Off()
            x = x + 1

    def Set_Column_Off (self, column):
        x = 0
        while x < self.LEDNum:
            LEDx = self.LEDs[x].getX()
            if LEDx == column:
                self.LEDs[x].Off()
            x = x + 1