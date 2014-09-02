from naoqi import ALProxy
import sys, os

if __name__ == "__main__":
	IP, PORT = "127.0.0.1", 9559
	os.system("python stiffness.py 1")
	postureProxy = ALProxy("ALRobotPosture", IP, PORT)
	postureProxy.goToPosture("LyingBelly", 0.8)
	os.system("python stiffness.py 0")
