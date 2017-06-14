import DobotCoordinates
from DobotSDK import Dobot
dobot = Dobot('COM5', debug=False)
dobot.CalibrateJoint(1, dobot.freqToCmdVal(500), dobot.freqToCmdVal(50), 1, 5, 1, 0)
dobot.InitializeAccelerometers()

upP,acceleration,speed = 100,400,400

class Methods():          
    def touchTest(self,device,station):
        print "Touch test started..."
        [x1,x2,x4],[y1,y2,y4] = DobotCoordinates.getZeroPoint(device,station)
        height,width,down,up = self.getPhoneProperties(device)
        numberOfSquareX = 16
        numberOfSquareY = 9
        shiftY = y2 - y1
        shiftX = x4 - x1
        xRange = (x2 - x1) / numberOfSquareX
        yRange = (y4 - y1) / numberOfSquareY
        xBuffer = (xRange / 2.0)
        yBuffer = (yRange / 2.0)
        for stepX in range(0,numberOfSquareX):
            x = x1 + xRange * stepX + xBuffer
            for stepY in range(0, numberOfSquareY):
                y = y1 + yRange * stepY + yBuffer + stepX * (shiftY/numberOfSquareX)
                x = x + shiftX/numberOfSquareY
                dobot.MoveWithSpeed(x, y, up, speed, acceleration)
                dobot.MoveWithSpeed(x, y, down, speed, acceleration)
                dobot.MoveWithSpeed(x, y, up, speed, acceleration)

    def my_range(start, end, step):
        while start <= end:
            yield start
            start += step
            
    def pushTouchTestStartButton(self,device,station):
        [x1,x2,x4],[y1,y2,y4] = DobotCoordinates.getZeroPoint(device,station)
        height,width,down = getPhoneProperties(device)
        print "Touch button pushed"
        dobot.MoveWithSpeed(x1 + 105, y1 + 34, up, speed, acceleration)
        dobot.MoveWithSpeed(x1 + 105, y1 + 34, down, speed, acceleration)
        dobot.MoveWithSpeed(x1 + 105, y1 + 34, up, speed, acceleration)
                
    def pushCoordinate(self,x,y,device):
        height,width,down,up = self.getPhoneProperties(device)
        dobot.MoveWithSpeed(x, y, up, speed, acceleration)
        dobot.MoveWithSpeed(x, y, down, speed, acceleration)
        print "pushed coordinates are, x:",x," y:",y
        #raw_input("Press Enter to go home..1.")
        dobot.MoveWithSpeed(x, y, up, speed, acceleration)
     
    def readScenario(self,filename): # accomplished
        mynumbers = []
        with open(filename) as f:
            for line in f:
                mynumbers.append([int(n) for n in line.strip().split(',')])              
        return mynumbers
    
    def androidToDobot(self,xA,yA,device,station): # accomplished
        height,width,down,up = self.getPhoneProperties(device)
        [x1,x2,x4],[y1,y2,y4] = DobotCoordinates.getZeroPoint(device,station)
        print x1,x2,x4,y1,y2,y4
        y = xA # Change android coordinate system to dobot
        x = height - yA       
        xDobotCor = (x2-x1)*(x/height) + (x4-x1)*(y/width)
        yDobotCor = (y4-y1)*(y/width) + (y2-y1)*(x/height)
        return x1+xDobotCor,y1+yDobotCor
    
    def goUp(self,x,y):
        dobot.MoveWithSpeed(x, y, upP, speed, acceleration)

    def goHome(self):# accomplished    
        #go to home
        print "I'm going home :)"
        dobot.MoveWithSpeed(240, -20, 80, speed, acceleration) 
    
    def getPhoneProperties(self,device):
        if (device == "Pars"):
            height = 1280.0
            width = 720.0
            down = 49.0
            
        if (device == "Reys"):
            height = 1920.0
            width = 1080.0
            down = 50.3
        up = down + 3.0
        return height,width,down,up
            
    



