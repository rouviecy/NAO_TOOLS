import sys, time
from naoqi import ALProxy
from Postures import Postures

IP, PORT = "127.0.0.1", 9559

motionProxy = ALProxy("ALMotion", IP, PORT)
commandAngles = motionProxy.getAngles("Body", False)

postures = Postures()

postures.stiffness(True)
time.sleep(5)

motionProxy.setAngles("Body", commandAngles, 0.5)

postures.stiffness(False)
