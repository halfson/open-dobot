#from dobot.DobotHakanSDK import *
from dobot.DobotHakanSDK import Methods
from dobot import DobotCoordinates

methods = Methods()
testCycleNumber = 10
stations = [4,5]
device = ["Pars","Pars"]
steps = methods.readScenario("senaryo1.txt")

for x in range (0,testCycleNumber):
    for i in range(0,len(stations)):        
        for k in range (0,len(steps)):
            (a,b) = methods.androidToDobot(steps[k][0],steps[k][1],device[i],stations[i])
            if (k==0):
                methods.goUp(a,b)
            methods.pushCoordinate(a,b,device[i])
        methods.goUp(a,b)
methods.goHome()

#===============================================================================
# stations = [1,2,3]
# device = ["pars","pars","pars"]
#===============================================================================

#===============================================================================
# stations = [5]
# device = ["pars"]
#===============================================================================

#===============================================================================
# xy = methods.readCoordinates("senaryo1.txt")
# print xy
# for x in range (0,testCycleNumber):
#     for i in range(0,len(stations)):
#         [x1, x2, x4], [y1, y2, y4] = DobotCoordinates.Coordinates(device[i], stations[i])
#         methods.goUp(x1,y1)
#         for k in range (0,len(xy)):
#             (height,width,down) = methods.getPhoneProperties(device[i])            
#             #androidToDobot(self,xA,yA,height,width,x1,x2,x4,y1,y2,y4)
#             #print xy[k][0],xy[k][1]
#             (a,b) = methods.androidToDobot(xy[k][0],xy[k][1],device,station)
#             methods.pushCoordinate(a,b,down)
#         methods.goUp(a,b)
# methods.goHome()
#===============================================================================
#===============================================================================
# for cycle in range(0, testCycleNumber):
#     print testCycleNumber
#     methods.pushTouchTestStartButton(x1,y1)
#     methods.touchTest(x1,y1,x2,y2,x4,y4)
#===============================================================================

