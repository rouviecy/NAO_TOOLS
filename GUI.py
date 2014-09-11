# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from Configuration import Configuration as c

class GUI(object):

	def __init__(self, serveur):
		self.joystick_WE = 0
		self.joystick_NS = 0
		self.joystick_ROT = 0
		self.clock = pygame.time.Clock()
		self.serveur = serveur
		self.initialisation()
		self.rafraishissement()
		self.bouclage()
		self.serveur.quitter()

	def initialisation(self):
		pygame.init()
		fenetre = pygame.display.set_mode((640, 480))
		nb = pygame.joystick.get_count()
		print str(nb) + " joystick(s) détectés"
		if(nb > 0):
			print "Activation du 1er joystick"
			mon_joystick = pygame.joystick.Joystick(0)
			mon_joystick.init()
			return True
		return False

	def rafraishissement(self):
		pygame.display.flip()

	def action_clavier(self, downing, key):
		if		key == c.K_QUIT:					return False
		elif	key == c.K_LEFT:					self.serveur.go_left(downing)
		elif	key == c.K_RIGHT:					self.serveur.go_right(downing)
		elif	key == c.K_NORTH:					self.serveur.go_north(downing)
		elif	key == c.K_SOUTH:					self.serveur.go_south(downing)
		elif	key == c.K_STIFFON:
			if downing:								self.serveur.stiffness(True)
		elif	key == c.K_STIFFOFF:
			if downing:								self.serveur.stiffness(False)
		elif	key == c.K_SAVE_JOINTS:
			if downing:								self.serveur.save_joints(True)
		elif	key == c.K_PLAY_JOINTS:
			if downing:								self.serveur.save_joints(False)
		elif	key == c.K_RECORD:
			if downing:								self.serveur.record()
		return True

	def action_joystick_bouton(self, bouton):
		if		bouton == c.J_BUTTON_A:	self.serveur.assis()
		elif	bouton == c.J_BUTTON_B:	self.serveur.debout()
		return True

	def action_joystick_axe(self, axe, valeur):
		if axe == c.J_AXIS_WE:
			if		c.J_INTERVAL_W[0] <= valeur <= c.J_INTERVAL_W[1]:
				if		self.joystick_WE == 0:
					self.joystick_WE = -1
					self.serveur.go_west(True)
				elif	self.joystick_WE == 1:
					self.joystick_WE = -1
					self.serveur.go_est(False)
					self.serveur.go_west(True)
			elif	c.J_INTERVAL_E[0] <= valeur <= c.J_INTERVAL_E[1]:
				if		self.joystick_WE == 0:
					self.joystick_WE = +1
					self.serveur.go_est(True)
				elif	self.joystick_WE == -1:
					self.joystick_WE = +1
					self.serveur.go_west(False)
					self.serveur.go_est(True)
			elif	c.J_INTERVAL_0WE[0] <= valeur <= c.J_INTERVAL_0WE[1]:
				if		self.joystick_WE == -1:
					self.joystick_WE = 0
					self.serveur.go_west(False)
				elif	self.joystick_WE == +1:
					self.joystick_WE = 0
					self.serveur.go_est(False)
		if		axe == c.J_AXIS_NS:
			if c.J_INTERVAL_N[0] <= valeur <= c.J_INTERVAL_N[1]:
				if		self.joystick_NS == 0:
					self.joystick_NS = -1
					self.serveur.go_north(True)
				elif	self.joystick_NS == 1:
					self.joystick_NS = -1
					self.serveur.go_south(False)
					self.serveur.go_north(True)
			elif	c.J_INTERVAL_S[0] <= valeur <= c.J_INTERVAL_S[1]:
				if		self.joystick_NS == 0:
					self.joystick_NS = +1
					self.serveur.go_south(True)
				elif	self.joystick_NS == -1:
					self.joystick_NS = +1
					self.serveur.go_north(False)
					self.serveur.go_south(True)
			elif	c.J_INTERVAL_0NS[0] <= valeur <= c.J_INTERVAL_0NS[1]:
				if		self.joystick_NS == -1:
					self.joystick_NS = 0
					self.serveur.go_north(False)
				elif	self.joystick_NS == +1:
					self.joystick_NS = 0
					self.serveur.go_south(False)
		if		axe == c.J_AXIS_ROT:
			if c.J_INTERVAL_L[0] <= valeur <= c.J_INTERVAL_L[1]:
				if		self.joystick_ROT == 0:
					self.joystick_ROT = -1
					self.serveur.go_left(True)
				elif	self.joystick_ROT == 1:
					self.joystick_ROT = -1
					self.serveur.go_right(False)
					self.serveur.go_left(True)
			elif	c.J_INTERVAL_R[0] <= valeur <= c.J_INTERVAL_R[1]:
				if		self.joystick_ROT == 0:
					self.joystick_ROT = +1
					self.serveur.go_right(True)
				elif	self.joystick_ROT == -1:
					self.joystick_ROT = +1
					self.serveur.go_left(False)
					self.serveur.go_right(True)
			elif	c.J_INTERVAL_0ROT[0] <= valeur <= c.J_INTERVAL_0ROT[1]:
				if		self.joystick_ROT == -1:
					self.joystick_ROT = 0
					self.serveur.go_left(False)
				elif	self.joystick_ROT == +1:
					self.joystick_ROT = 0
					self.serveur.go_right(False)
		return True

	def bouclage(self):
		continuer = True
		while continuer:
			for event in pygame.event.get():
				if		event.type == QUIT:				continuer = False
				elif	event.type == KEYDOWN:			continuer = self.action_clavier(True, event.key)
				elif	event.type == KEYUP:			continuer = self.action_clavier(False, event.key)
				elif	event.type == JOYBUTTONDOWN:	continuer = self.action_joystick_bouton(event.button)
				elif	event.type == JOYAXISMOTION:	continuer = self.action_joystick_axe(event.axis, event.value)
			self.clock.tick(20)
