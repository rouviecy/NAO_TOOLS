import sys

class IO_file(object):

	def __init__(self):
		a = 42

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
			elems = ligne.split("\n")[0].split(" ")
			elems = [float(elem) for elem in elems]
			liste.append([elems[0], elems[1:len(elems)]])
		return liste
