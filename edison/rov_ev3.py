from uart import SerialManager

#in1 <--> rov station
#in2 <--> arduino (compass, depth)

class Motor():
	MOTOR_L = 0
	MOTOR_R = 1
	MPTPR_LU = 2
	MPTPR_RU = 3
	
	def __init(self, motor_id):
		self.id = motor_id
		if 
	def power(self, target):
	def direction(self, cmd):
class ROV():

	
	def __init__(self):
		self.motors = [Motor()]