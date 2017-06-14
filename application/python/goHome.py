from dobot import Dobot

# Acceleration in mm/s^2
acceleration = 20
speed = 20

dobot = Dobot('COM5', debug=False)
dobot.CalibrateJoint(1, dobot.freqToCmdVal(500), dobot.freqToCmdVal(50), 1, 5, 1, 0)
dobot.InitializeAccelerometers()

#===============================================================================
# dobot = Dobot('COM5', debug=True)
# dobot.CalibrateJoint(1, dobot.freqToCmdVal(500), dobot.freqToCmdVal(50),1 , 5, 1, 0)
# dobot.InitializeAccelerometers()
#===============================================================================

#dobot.MoveWithSpeed(260, -10, 80, speed, acceleration)

#go home
#raw_input("Press Enter to go home...")

dobot.MoveWithSpeed(240, -20, 80, speed, acceleration)