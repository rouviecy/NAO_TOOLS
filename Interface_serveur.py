# -*- coding: utf-8 -*-

from threading import Thread
import socket
import select
import time

class Interface_serveur(object):
	
	def __init__(self, port):
		host = ''
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((host, port))
		print("Écoute sur le port {}".format(port))
		self.liste_clients = []
		self.liste_threads = Thread_serveur(self)
		self.liste_threads.start()

	def go_left(self, activer):		self.envoyer("gl" + ("1" if activer else "0"))
	def go_right(self, activer):	self.envoyer("gr" + ("1" if activer else "0"))
	def go_north(self, activer):	self.envoyer("gn" + ("1" if activer else "0"))
	def go_south(self, activer):	self.envoyer("gs" + ("1" if activer else "0"))
	def go_west(self, activer):		self.envoyer("gw" + ("1" if activer else "0"))
	def go_est(self, activer):		self.envoyer("ge" + ("1" if activer else "0"))
	def stiffness(self, activer):	self.envoyer("st" + ("1" if activer else "0"))
	def save_joints(self, save):	self.envoyer("sa" + ("1" if save else "0"))
	def record(self):				self.envoyer("rec")
	def assis(self):				self.envoyer("po0")
	def debout(self):				self.envoyer("po1")
	def quitter(self):
		self.envoyer("bye")
		time.sleep(1)
		self.s.close()

	def envoyer(self, message):
		for client in self.liste_clients:
			client.send(message.encode())
		
class Thread_serveur(Thread):

	def __init__(self, serveur):
		Thread.__init__(self)
		self.serveur = serveur

	def run(self):
		self.serveur.s.listen(5)
		nouveau_client, _ = self.serveur.s.accept()
		self.serveur.liste_clients.append(nouveau_client)
