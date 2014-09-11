import socket

class Interface_client(object):

	def __init__(self, host, actionneur):
		self.actionneur = actionneur
		port = 4242
		self.ouvert = True
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((host, port))
		while self.ouvert:
			msg_in = self.s.recv(1024)
			self.decodage(msg_in)

		self.s.close()

	def decodage(self, msg):
		c = msg.decode()
		for i in range(len(c) / 3):
			if c == "bye":			self.ouvert = False
			elif c[3*i+0] == 'g':
				if		c[3*i+1] == 'l' :	self.go_left(c[3*i+2] == '1')
				elif	c[3*i+1] == 'r' :	self.go_right(c[3*i+2] == '1')
				elif	c[3*i+1] == 'n' :	self.go_north(c[3*i+2] == '1')
				elif	c[3*i+1] == 's' :	self.go_south(c[3*i+2] == '1')
				elif	c[3*i+1] == 'w' :	self.go_west(c[3*i+2] == '1')
				elif	c[3*i+1] == 'e' :	self.go_est(c[3*i+2] == '1')
			elif c[3*i+0] == 'p':
				if		c[3*i+1] == 'o' :
					if		c[3*i+2] == '0' :	self.assis()
					elif	c[3*i+2] == '1' :	self.debout()
			elif c[3*i+0] == 's':
				if		c[3*i+1] == 't' :
					if		c[3*i+2] == '0' :	self.stiffness(False)
					elif	c[3*i+2] == '1' :	self.stiffness(True)
				elif	c[3*i+1] == 'a' :
					if		c[3*i+2] == '0' :	self.save_joints(False)
					elif	c[3*i+2] == '1' :	self.save_joints(True)

	def go_left(self, activer):		self.actionneur.go_left(activer)
	def go_right(self, activer):	self.actionneur.go_right(activer)
	def go_north(self, activer):	self.actionneur.go_north(activer)
	def go_south(self, activer):	self.actionneur.go_south(activer)
	def go_west(self, activer):		self.actionneur.go_west(activer)
	def go_est(self, activer):		self.actionneur.go_est(activer)
	def stiffness(self, activer):	self.actionneur.stiffness(activer)
	def assis(self):				self.actionneur.assis()
	def debout(self):				self.actionneur.debout()
	def save_joints(self, save):	self.actionneur.save_joints(save)
