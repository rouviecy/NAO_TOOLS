# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

def initialisation():
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

def rafraishissement():
	pygame.display.flip()

def bouclage():
	continuer = True
	while continuer:
		for event in pygame.event.get():
			if		event.type == QUIT:
				continuer = False
			elif	event.type == KEYDOWN:
				print "Appui sur la touche :\t" + str(event.key)
			elif	event.type == JOYBUTTONDOWN:
				print "Appui sur le bouton joystick :\t" + str(event.button)
			elif	event.type == JOYAXISMOTION:
				print "Mouvement d'axe :\t" + str(event.axis) + "\tà la position :\t" + str(event.value)
			elif	event.type == JOYHATMOTION:
				print "Mouvement du pointeur :\t" + str(event.hat) + "\tà la position :\t" + str(event.value)
		continue;

if __name__ == "__main__":
	initialisation()
	rafraishissement()
	bouclage()
