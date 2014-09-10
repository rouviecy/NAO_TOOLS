import sys

class IO_file(object):

	def __init__(self):
		pass

	def write_joints(self, joints, dt):
		f = open('historique.txt', 'a')
		ligne = str(dt)
		for joint in joints:
			ligne += " " + str(joint)
		ligne += "\n"
		f.write(ligne)
		f.close()

	def read_joints(self):
		f = open('historique.txt', 'r')
		liste = []
		for ligne in f:
			elems = ligne.split(" ")
			liste.append(elems)
		return liste
