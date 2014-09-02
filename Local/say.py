from naoqi import ALProxy
import sys

def verif_args():
	if len(sys.argv) == 2 : return True
	print "Utilisation :\n\tpython say.py \"texte\""
	return False

if __name__ == "__main__":
	if not verif_args(): exit()
	IP, PORT = "127.0.0.1", 9559
	c3po = ALProxy("ALTextToSpeech", IP, PORT)
	texte = sys.argv[1]
	c3po.say(texte)
