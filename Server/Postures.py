from naoqi import ALProxy
import sys

class Postures(object):

	def __init__(self):
		IP, PORT = "127.0.0.1", 9559
		self.postureProxy = ALProxy("ALRobotPosture", IP, PORT)
		self.motionProxy = ALProxy("ALMotion", IP, PORT)

	def stiffness(self, go_rigide):
		parametre = 1.0 if go_rigide else 0.0
		self.motionProxy.stiffnessInterpolation("Body", parametre, 1.0)

	def go_debout(self):
		self.stiffness(True)
		self.postureProxy.goToPosture("Stand", 0.8)

	def go_assis(self):
		self.stiffness(True)
		self.postureProxy.goToPosture("Sit", 0.8)
		self.stiffness(False)

	def go_ventre(self):
		self.stiffness(True)
		self.postureProxy.goToPosture("LyingBelly", 0.8)
		self.stiffness(False)

	def go_dos(self):
		self.stiffness(True)
		self.postureProxy.goToPosture("LyingBack", 0.8)
		self.stiffness(False)

	def go_dos(self):
		self.stiffness(True)
		self.postureProxy.goToPosture("Crouch", 0.8)
		self.stiffness(False)
