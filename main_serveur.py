from GUI				import GUI
from Interface_serveur	import Interface_serveur
import sys

if __name__ == '__main__':
	serveur = Interface_serveur(int(sys.argv[1]))
	gui = GUI(serveur)
