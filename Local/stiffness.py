from naoqi import ALProxy
import sys

def verif_args():
	if len(sys.argv) == 2:
		parametre = int(sys.argv[1])
		if parametre == 0 or parametre == 1 return True
	print "Utilisation :\n\tpython stiffness.py 0/1"
	return False

if __name__ == "__main__":
	if not verif_args(): exit()
	IP, PORT = "127.0.0.1", 9559
	parametre = 1.0 if int(sys.argv[1]) else 0.0
	motionProxy = ALProxy("ALMotion", IP, PORT)
	motionProxy.stiffnessInterpolation("Body", parametre, 1.0)
