import sys

class IO_file(object):

	def __init__(self):
		self.lignes = ""

	def init_write_joints(self):
		return open('historique.txt', 'a')

	def add_joints(self, joints, dt):
		ligne = str(dt)
		for joint in joints:
			ligne += " " + str(joint)
		ligne += "\n"
		self.lignes += ligne

	def write_joints(self, fichier):
		fichier.write(self.lignes)
		fichier.close()
		self.lignes = ""

	def read_joints(self, only_last):
		f = open('historique.txt', 'r')
		t = 0
		liste_temps = []
		liste_angles = []
		for ligne in f:
			elems = ligne.split("\n")[0].split(" ")
			if len(elems) < 5: continue
			elems = [float(elem) for elem in elems]
			t += elems[0]
			liste_temps.append(t)
			liste_angles.append(elems[1:len(elems)])
		temps = []
		angles = []
		if len(liste_angles) == 0: return [], []
		if only_last:
			last_index = len(temps) - 1
			liste_temps = [1.]
			liste_angles = [liste_angles[last_index]]
		for i in range(len(liste_angles[0])):
			joint = [liste_angles[j][i] for j in range(len(liste_angles))]
			vect_t = [liste_temps[j] for j in range(len(liste_angles))]
			angles.append(joint)
			temps.append(vect_t)
		return temps, angles
