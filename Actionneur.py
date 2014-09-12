from naoqi import ALProxy
from Mouvements import Mouvements
import os

class Actionneur(object):

	def __init__(self):
		self.rotation = 0
		self.avance = 0
		self.cote = 0
		self.move = Mouvements()

	def go_left(self, activer):		self.modifier_vitesse(0, 0, +1 if activer else -1)
	def go_right(self, activer):	self.modifier_vitesse(0, 0, -1 if activer else +1)
	def go_north(self, activer):	self.modifier_vitesse(+1 if activer else -1, 0, 0)
	def go_south(self, activer):	self.modifier_vitesse(-1 if activer else +1, 0, 0)
	def go_west(self, activer):		self.modifier_vitesse(0, +1 if activer else -1, 0)
	def go_est(self, activer):		self.modifier_vitesse(0, -1 if activer else +1, 0)
	def stiffness(self, activer):	self.move.stiffness(activer)
	def record(self):				self.move.record()
	def assis(self):				self.move.go_assis()
	def debout(self):				self.move.go_debout()
	def save_joints(self, save):
		if save:					self.move.save_joints(True)
		else:						self.move.apply_joints_from_file()
	def vitesse_tete(self, vx, vy):	self.move.move_head(vx, vy)

	def modifier_vitesse(self, dx, dy, dth):
		self.rotation += dth
		self.avance += dx
		self.cote += dy
		print "vx =", self.avance, "\tvy =", self.cote, "\tvth =", self.rotation
		print "------------------------------------------------"
		if		self.avance == +1:		self.move.set_vx(+0.7)
		elif	self.avance == -1:		self.move.set_vx(-0.7)
		else:							self.move.set_vx(+0.0)
		if		self.cote == +1:		self.move.set_vy(+0.7)
		elif	self.cote == -1:		self.move.set_vy(-0.7)
		else:							self.move.set_vy(+0.0)
		if		self.rotation == +1:	self.move.set_vth(+0.7)
		elif	self.rotation == -1:	self.move.set_vth(-0.7)
		else:							self.move.set_vth(+0.0)
		self.move.go_move()

	def quitter(self):
		pass;
