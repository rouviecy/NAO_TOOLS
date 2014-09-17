from threading import Thread
import time

class Recorder(Thread):

	def __init__(self, mouvements):
		Thread.__init__(self)
		self.mouvements = mouvements
		self.continuer = False

	def run(self):
		fichier = self.mouvements.io_file.init_write_joints()
		while self.continuer:
			self.mouvements.save_joints(False)
			time.sleep(self.mouvements.dt)
		self.mouvements.io_file.write_joints(fichier)
