from naoqi import ALProxy
from IO_file import IO_file
import sys, time

class Mouvements(object):

	def __init__(self):
		IP, PORT = "127.0.0.1", 9559
		self.vx = 0.0
		self.vy = 0.0
		self.vth = 0.0
		self.joints = []
		self.io_file = IO_file()
		self.postureProxy = ALProxy("ALRobotPosture", IP, PORT)
		self.motionProxy = ALProxy("ALMotion", IP, PORT)
		self.motionProxy.setWalkArmsEnabled(True, True)
		self.motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])

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

	def go_move(self):
		self.motionProxy.setWalkTargetVelocity(self.vx, self.vy, self.vth, 0.8)

	def set_vx(self, vx):	self.vx = vx
	def set_vy(self, vy):	self.vy = vy
	def set_vth(self, vth):	self.vth = vth

	def update_joints(self):	self.joints = self.motionProxy.getAngles("Body", False)
	def set_joints(self):		self.motionProxy.setAngles("Body", self.joints, 0.5)

	def save_joints(self):
		self.update_joints()
		self.io_file.write_joints(self.joints, 1.)

	def apply_joints_from_file(self):
		liste = self.io_file.read_joints()
		for elem in liste:
			self.joints = elem[1]
			self.set_joints()
			time.sleep(elem[0])
