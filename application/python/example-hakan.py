#! /usr/bin/env python
import time
from dobot import Dobot
dobot = Dobot('COM3', debug=True)

down=49.0
up=53
acceleration = 450 # Acceleration in mm/s^2
speed = 450
dobot.CalibrateJoint(1, dobot.freqToCmdVal(50), dobot.freqToCmdVal(50), 1, 5, 1, 0)
dobot.InitializeAccelerometers()

testCycleNumber = 1000

# # PARS
# ph4x1 = 110.5  # phone 4 x1 position
# ph4x2 = ph4x1 + 123.4  # phone 4 x2 position #real length = 12.1cm
# ph4x4 = ph4x1 + 1.0
#
# ph4y1 = 133.0  # phone 4 y1 position
# ph4y2 = ph4y1 - 2.7  # ph4y2 = ph4y1 + 68.1  # phone 4 y2 position #real length = 6.8cm
# ph4y4 = ph4y1 + 67.6

# ORCA
ph4x1 = 108.5  # phone 4 x1 position
ph4x2 = ph4x1 + 123.3  # phone 4 x2 position #real length = 12.1cm
ph4x4 = ph4x1 + 1.1

ph4y1 = 133.0  # phone 4 y1 position
ph4y2 = ph4y1 - 2.7  # ph4y2 = ph4y1 + 68.1  # phone 4 y2 position #real length = 6.8cm
ph4y4 = ph4y1 + 67.7

shiftY = ph4y2 - ph4y1
shiftX = ph4x4 - ph4x1

numberOfSquareX = 16
numberOfSquareY = 9

xRange = (ph4x2-ph4x1)/numberOfSquareX
yRange = (ph4y4-ph4y1)/numberOfSquareY

xBuffer = (xRange/2.0)
yBuffer = (yRange/2.0)

def pushTouchTestStartButton():
    dobot.MoveWithSpeed(ph4x1 + 105, ph4y1 + 34, up, speed, acceleration)
    dobot.MoveWithSpeed(ph4x1 + 105, ph4y1 + 34, down, speed, acceleration)
    dobot.MoveWithSpeed(ph4x1 + 105, ph4y1 + 34, up, speed, acceleration)
def TouchTest(x1,y1,xxRange,yyRange,xxBuffer,yyBuffer,upp,downn,speedd,accelerationn,numberOfSquareXX,numberOfSquareYY,shiftXX,shiftYY):

    for stepX in range(0,numberOfSquareXX):
        x = x1 + xxRange * stepX + xxBuffer
        for stepY in range(0, numberOfSquareYY):
            y = y1 + yyRange * stepY + yyBuffer + stepX * (shiftYY/numberOfSquareXX)
            x = x + shiftXX/numberOfSquareYY

            dobot.MoveWithSpeed(x, y, upp, speedd, accelerationn)
            dobot.MoveWithSpeed(x, y, downn, speed, accelerationn)
            dobot.MoveWithSpeed(x, y, upp, speed, accelerationn)
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
for cycle in range(0, testCycleNumber):
    print testCycleNumber
    pushTouchTestStartButton()
    TouchTest(ph4x1,ph4y1,xRange,yRange,xBuffer,yBuffer, up, down,speed, acceleration, numberOfSquareX,numberOfSquareY,shiftX, shiftY)
    dobot.Wait(10)
#
# dobot.MoveWithSpeed(ph4x1, ph4y1, up, speed, acceleration)#start point control x1,y1
# raw_input("Press Enter to continue...")
#
# dobot.MoveWithSpeed(ph4x2, ph4y2, up, speed, acceleration)#x2,y2
# raw_input("Press Enter to continue...")
#
# dobot.MoveWithSpeed(ph4x4, ph4y4, up, speed, acceleration)#x4,y4
# raw_input("Press Enter to continue...")

#go to home
#raw_input("Press Enter to go home...")
dobot.MoveWithSpeed(260, -20, 80, speed, acceleration)

