from threading import Thread
import time

class Recorder(Thread):

	def __init__(self, mouvements):
		Thread.__init__(self)
		self.mouvements = mouvements
		self.continuer = False

	def run(self):
		while self.continuer:
			self.mouvements.save_joints()
			time.sleep(0.1)
