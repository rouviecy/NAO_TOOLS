from naoqi import ALProxy
from Mouvements import Mouvements
import os

class Actionneur(object):

	def __init__(self):
		self.rotation = 0
		self.avance = 0
		self.move = Mouvements()

	def go_left(self, activer):		self.modifier_vitesse(-1 if activer else +1, 0)
	def go_right(self, activer):	self.modifier_vitesse(+1 if activer else -1, 0)
	def go_up(self, activer):		self.modifier_vitesse(0, +1 if activer else -1)
	def go_down(self, activer):		self.modifier_vitesse(0, -1 if activer else +1)
	def assis(self):				self.move.go_assis()
	def debout(self):				self.move.go_debout()

	def modifier_vitesse(self, dx, dy):
		self.rotation += dx
		self.avance += dy
		str_rot = "reste dans l'axe"
		str_av = "reste sur place"
		if self.rotation < 0: str_rot = "va a gauche"
		if self.rotation > 0: str_rot = "va a droite"
		if self.avance < 0: str_av = "recule"
		if self.avance > 0: str_av = "avance"
		print str_rot + " et " + str_av
		if		self.avance == +1:		self.move.set_vx(+0.7)
		elif	self.avance == -1:		self.move.set_vx(-0.7)
		else:							self.move.set_vx(+0.0)
		if		self.rotation == +1:	self.move.set_vth(-0.7)
		elif	self.rotation == -1:	self.move.set_vth(+0.7)
		else:							self.move.set_vth(-0.0)
		self.move.go_move()
		print "------------------------------------------"

	def quitter(self):
		pass;
