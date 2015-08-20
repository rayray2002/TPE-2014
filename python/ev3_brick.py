import bluetooth, time, sys, os
from struct import *
import math
import socket
import pickle


class Command:
	seq = 0
	opOUTPUT_POLARITY = 0xA7
	opOUTPUT_START = 0xA6
	opOUTPUT_STOP = 0xA3
	opOUTPUT_SPEED = 0xA5
	opOUTPUT_MAILBOX = 0x9E #mail box
	opINPUT_DEVICE_LIST = 0x98
	opINPUT_READ = 0x9A
	opINPUT_READSI = 0x9D
	opINPUT_DEVICE = 0x99	
	opSound = 0x94
	opOUTPUT_CLR_COUNT = 0xB2
	opOUTPUT_GET_COUNT = 0xB3 
	
	opUIREAD = 0x81
	
	DIRECT_COMMAND_REPLY = 0x00
	DIRECT_COMMAND_NO_REPLY = 0x81
		
	def __init__(self):		
		self.seq = Command.seq
		self.msg = bytearray(b"")
		self.msg.append(0) #length
		self.msg.append(0) #length
		self.msg.append(0) #seq
		self.msg.append(0) #seq				
		self.msg[2] = self.seq&0xFF
		self.msg[3] = (self.seq&0xFF00) / 256
		Command.seq += 1
		
	def opcode(self, op, force_size=0):
		if op==Command.opINPUT_DEVICE_LIST:
			self.msg.append(Command.DIRECT_COMMAND_REPLY) #reply
			self.msg.append(5) #reply size
			self.msg.append(0) 
		elif op==Command.opINPUT_DEVICE or op==Command.opINPUT_READ:
			self.msg.append(Command.DIRECT_COMMAND_REPLY) #reply
			if force_size: self.msg.append(force_size)
			else: self.msg.append(1) #reply size
			self.msg.append(0)
		elif op==Command.opOUTPUT_GET_COUNT or op==Command.opUIREAD or op==Command.opINPUT_READSI:
			self.msg.append(Command.DIRECT_COMMAND_REPLY) #reply
			self.msg.append(4) #reply size
			self.msg.append(0)
		elif op==Command.opOUTPUT_MAILBOX:
			self.msg.append(Command.DIRECT_COMMAND_NO_REPLY) #no reply
		else:
			self.msg.append(Command.DIRECT_COMMAND_NO_REPLY) #no reply
			self.msg.append(0) #reseved
			self.msg.append(0) #reseved
			
		self.msg.append(op)
		
	def LC0(self, param):
		self.msg.append(param)
		
	def LC1(self, param):
		self.msg.append(0x81)
		self.msg.append(param)	
		
	def LC2(self, param):
		self.msg.append(0x82)
		self.msg.append(param&0xFF)		
		self.msg.append((param&0xFF00) / 256)	
		
	def GV0(self, param):
		self.msg.append(param)
		
	def send(self):
		size = len(self.msg) -2
		self.msg[0] = size & 0xFF
		self.msg[1] = size & 0xFF / 256				
		return str(self.msg)
		
class EV3Brick:	
	STATE_CONNECTING = 1
	STATE_CONNECTED = 2
	STATE_DISCONNECTED = 3
	MOTOR_A = 1
	MOTOR_B = 2
	MOTOR_C = 4
	MOTOR_D = 8
	MOTOR_ALL = MOTOR_A|MOTOR_B|MOTOR_C|MOTOR_D
	
	INPUT_UNKNOWN = 0
	INPUT_NXT_TOUCH = 1
	INPUT_NXT_Light = 2
	INPUT_NXT_SOUND = 3
	INPUT_NXT_COLOR = 4
	INPUT_NXT_ULTRASONIC = 5
	INPUT_NXT_Temperature = 6
	INPUT_LMotor = 7
	INPUT_MMotor = 8
	
	INPUT_TOUCH = 16
	INPUT_TEST = 21	
	INPUT_COLOR = 29
	INPUT_ULTRASONIC = 30
	INPUT_GYRO = 32
	INPUT_IR = 33
	INPUT_I2C = 100	
	INPUT_EMPTY = 126
		
	MODE_REFLECTED = 0
	MODE_AMBIENT = 1
	MODE_COlOR = 2
	
	def __init__(self):
		self.socket = None
		self.brick_bt = ''
		self.brick_name = ''
		self.state = EV3Brick.STATE_DISCONNECTED
		self.inputs = []
		self.input_values = []
		#self.outputs = []
		self.output_values = [] 
		self.seq = 0	
		self.color_mode = EV3Brick.MODE_COlOR

	def load_bt_devices(self, ev3name, refresh=False):
		bt_addr = None
		devices = {}
		try:
			devices = pickle.load(open('devices.obj', 'rb'))
			bt_addr = devices[ev3name]
			print 'bt_addr from cached', ev3name, bt_addr
			if not refresh: return bt_addr
		except Exception, e: print type(e), e
		
		print 'discovering..'
		nearby_devices = bluetooth.discover_devices(lookup_names = True)				
		for addr, name in nearby_devices:
			devices[name] = addr
			print("found:  %s - %s" % (addr, name))
		pickle.dump(devices, open('devices.obj', 'wb'))
		bt_addr = devices[ev3name]
		return bt_addr
						
	def connect(self, name=None):
		try:			
			self.disconnect()
			self.state = EV3Brick.STATE_CONNECTING
			if name: self.bt_name = name
			else:				
				username = os.getenv('USERNAME').lower()
				self.bt_name = username
				if username[-2] == '0': self.bt_name = username[:-2] + username[-1]		
			
			self.brick_bt = self.load_bt_devices(self.bt_name)			
			print 'brick_bt', self.brick_bt
			services = bluetooth.find_service(address=self.brick_bt)
			for s in services: print s						
			self.socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )		
			self.socket.connect((self.brick_bt, 1))
			self.state = EV3Brick.STATE_CONNECTED
			self.query_input_devices()
			print 'connected', name
		except IOError, e:
			print type(e), e
			self.state = EV3Brick.STATE_DISCONNECTED
			self.load_bt_devices(self.bt_name, refresh=True)
		
	def query_input_devices(self):		
		cmd = Command()
		cmd.opcode(Command.opINPUT_DEVICE_LIST)
		cmd.LC0(4) #length
		cmd.GV0(0x60) #array
		cmd.GV0(0x64) #changed
		reply = self.send(cmd)
		self.inputs = reply

	def find_port(self, input, scan=True):
		print 'find_port'
		if not self.inputs: self.query_input_devices()
		for idx in range(len(self.inputs)):
			if self.inputs[idx] == input: 				
				return idx
		if scan:
			self.query_input_devices()
			return self.find_port(input, scan=False)
		return 1 #fallback to port 1
	
		
	def disconnect(self):
		try:			
			self.socket.disconnect()
		except: pass		
	
	def keep_alive(self):
		pass
				
	def send(self, cmd):
		try:
			reply = []			
			self.socket.send(cmd.send())	
			#print 'send', cmd.msg
			if cmd.msg[4] == 0x00: #need reply
				b0 = self.socket.recv(1)
				b1 = self.socket.recv(1)
				size = ord(b1)*256+ord(b0)
				for c in self.socket.recv(size):										
					reply.append(ord(c))						
			return reply[3:] #skip: seq, seq, reply type
			
		except Exception: #IOError, TypeError		
			print 'socket exception'
			self.state = EV3Brick.STATE_DISCONNECTED			
			
	def get_motor(self, port):
		m =  int(math.pow(2, port))
		print 'get_motor', port, m
		return m
		
	def set_motor_direction(self, port, direction, layer=0):	
		cmd = Command()
		cmd.opcode(Command.opOUTPUT_POLARITY)
		cmd.LC0(layer) #layer
		cmd.LC0(self.get_motor(port)) #no
		cmd.LC0(1) #clockwise
		self.send(cmd)		
		if direction==-1:			
			cmd = Command()
			cmd.opcode(Command.opOUTPUT_POLARITY)
			cmd.LC0(0) #layer
			cmd.LC0(self.get_motor(port)) #no
			cmd.LC0(0) #toggle
			self.send(cmd)
		
	def set_motor_speed(self, port, speed, layer=0):	
		cmd = Command()
		cmd.opcode(Command.opOUTPUT_SPEED)
		cmd.LC0(layer) #layer
		cmd.LC0(self.get_motor(port)) #no
		cmd.LC1(speed) #
		self.send(cmd)				
		
	def motor_on(self, port, layer=0):
		print 'motor_on', port, layer
		cmd = Command()
		cmd.opcode(Command.opOUTPUT_START)
		cmd.LC0(layer) #layer
		cmd.LC0(self.get_motor(port)) #no		
		self.send(cmd)		
		
	def motor_off(self, port, layer=0, break_flag=1):
		print 'motor_on', port, layer
		cmd = Command()
		cmd.opcode(Command.opOUTPUT_STOP)
		cmd.LC0(layer) #layer
		cmd.LC0(self.get_motor(port)) #no
		cmd.LC0(break_flag) #break	
		self.send(cmd)		
		
	def reset_motor_position(self, port, layer=0):
		msg = bytearray(b"")
		msg.append(0) #length
		msg.append(0)
		msg.append(self.seq&0xFF)#sequence number
		msg.append(self.seq&0xFF00 / 256)
		msg.append(0x80)#Command type - system command without reply 0x81
		msg.append(0)
		msg.append(0)
		msg.append(0xA8) #opOUTPUT_READ
		msg.append(layer) #layer
		msg.append(port) #nos (motor)		
		msg[0] = len(msg) -2		
		self.socket.send(str(msg))		
		self.seq += 1
		
	def write_message(self, title, message): 
		print 'write_message', title, message
		print #https://wiki.qut.edu.au/display/cyphy/Mailbox+and+Messages
		cmd = Command()
		cmd.opcode(Command.opOUTPUT_MAILBOX)
		cmd.LC0(4) 
		cmd.LC0(ord('a') )
		cmd.LC0(ord('b') )
		cmd.LC0(ord('c') )
		cmd.LC0(0)

		cmd.LC0(7)
		cmd.LC0(0)
		cmd.LC0(ord('h') )
		cmd.LC0(ord('e') )
		cmd.LC0(ord('l') )
		cmd.LC0(ord('l') )
		cmd.LC0(ord('o') )
		cmd.LC0(ord('!') )
		cmd.LC0(0) #data
		print repr(cmd.msg)
		reply = self.send(cmd)	
						
	def display(self, x, y, text, clear=True):
		pass
	
	def light_on(self, color):
		pass
	
	def light_off(self, color):
		pass
	
	def read_sensors(self):			 
	 	self.input_values = []		
		
		for port in range(4):
			input_type = self.inputs[port]
			port += 1						
			if input_type == EV3Brick.INPUT_EMPTY:
				self.input_values.append((0,0,0))

			elif input_type == EV3Brick.INPUT_TOUCH or input_type==EV3Brick.INPUT_NXT_TOUCH:				
				self.input_values.append((EV3Brick.INPUT_TOUCH, port, self.read_touch(port)))
				
			elif input_type == EV3Brick.INPUT_GYRO:
				self.input_values.append((EV3Brick.INPUT_GYRO, port, self.read_gyro(port)))
				
			elif input_type == EV3Brick.INPUT_ULTRASONIC:
				self.input_values.append((EV3Brick.INPUT_ULTRASONIC, port, self.read_ultrasonic(port)))
				
			elif input_type == EV3Brick.INPUT_COLOR:				
				self.input_values.append((EV3Brick.INPUT_COLOR, port, self.read_color(port, mode=self.color_mode)))				
			else:
				print 'input_type', input_type
				#TODO: handle INPUT_MMotor, INPUT_LMotor				
								
		self.output_values = []
		for idx in range(4):
			#port = math.pow(2,idx)
			degree = self.get_motor_angle(idx+1)
			self.output_values.append((idx+1, degree))
		#print 'output_values', self.output_values
		return self.input_values	

	def read_color(self, port=0, mode=MODE_REFLECTED):				
		if port==0: port = self.find_port(EV3Brick.INPUT_COLOR)
		else: port -= 1	
		cmd = Command()
		cmd.opcode(Command.opINPUT_READSI)	
		cmd.LC0(0) #layer
		cmd.LC0(port) #port		
		cmd.LC0(29) #light		
		cmd.LC0(mode) #mode
		cmd.GV0(0x60)
		reply = self.send(cmd)		
		try:
			light = unpack('f', chr(reply[0])+chr(reply[1])+chr(reply[2])+chr(reply[3]))
			#print 'read_color light', light[0]	
			return int(light[0])
		except Exception, e:
			print type(e), e
			return 0				
		#Reflection = SensorMode.Mode0, Ambient = SensorMode.Mode1, Color = SensorMode.Mode2
	
	def read_ultrasonic(self, port=0):
		if port==0: port = self.find_port(EV3Brick.INPUT_ULTRASONIC)
		else: port -= 1
		cmd = Command()
		cmd.opcode(Command.opINPUT_READSI)	
		cmd.LC0(0) #layer
		cmd.LC0(port) #port		
		cmd.LC0(30) #ultrasonic		
		cmd.LC0(0) #mode
		cmd.GV0(0x60)
		reply = self.send(cmd)				
		try:
			dist = unpack('f', chr(reply[0])+chr(reply[1])+chr(reply[2])+chr(reply[3]))
			#print 'read_ultrasonic', dist[0]	
			return dist[0]
		except Exception, e:
			print type(e), e
			return 255
		
				
	def read_touch(self, port=0):
		if port==0: port = self.find_port(EV3Brick.INPUT_TOUCH)
		else: port -= 1		
		cmd = Command()
		cmd.opcode(Command.opINPUT_READ)
		cmd.LC0(0) #layer
		cmd.LC0(port) #port
		cmd.LC0(0) #DO_NOT_CHANGE_TYPE
		cmd.LC0(0) #MODE
		cmd.GV0(0x60) #GLOBAL_VAR_INDEX0
		reply = self.send(cmd)
		#print 'read_touch reply', reply
		if reply[0]==100: return 1
		else: return 0
		
	def read_gyro(self, port=0):
		if port==0: port = self.find_port(EV3Brick.INPUT_GYRO)
		else: port -= 1			
		cmd = Command()
		cmd.opcode(Command.opINPUT_READ)
		cmd.LC0(0) #layer
		cmd.LC0(port) #port
		cmd.LC0(0) #READY_SI
		cmd.LC0(0) #DO_NOT_CHANGE_TYPE
		cmd.GV0(0x60) #MODE_0
		reply = self.send(cmd)	
		#print 'read_gyro reply', port, reply		
		return reply[0]	
				
	def beep(self, freq=400, duration=1000):
		cmd = Command()
		cmd.opcode(Command.opSound)
		cmd.LC0(1) #TONE
		cmd.LC1(50) #Sound-level 0 ~255
		cmd.LC2(freq) #freq	
		cmd.LC2(duration) #duration	
		self.send(cmd)		
				
	def reset_motor_angle(self, port, layer=0):
		cmd = Command()
		cmd.opcode(Command.opOUTPUT_CLR_COUNT)
		cmd.LC0(layer) #layer
		cmd.LC0(self.get_motor(port)) #nos
		self.send(cmd)	
		
	def get_motor_angle(self, port):		
		cmd = Command()
		cmd.opcode(Command.opOUTPUT_GET_COUNT)
		cmd.LC0(0) #layer
		cmd.LC0(port-1) #no		
		cmd.GV0(0x60) #
		reply = self.send(cmd)
		#print 'get_motor_angle reply', reply		
		#print reply
		return reply[0] + reply[1]*256 + reply[2]*256*256 + reply[3]*256*256*256
		
	def get_battery_voltage(self):		
		cmd = Command()
		cmd.opcode(Command.opUIREAD)
		cmd.LC0(1) #1:GetVbatt subcode, 18:GetLBatt
		cmd.GV0(0x60) #
		reply = self.send(cmd)	
		print reply
		return unpack('f', chr(reply[0])+chr(reply[1])+chr(reply[2])+chr(reply[3]))
		
	def state(self):
		return self.state
		
#gyro reset
#temp get temp
# fix motor D

def main(hostname):	
	ev3 = EV3Brick()
	ev3.connect(name=hostname)
	port = 1
	print 'get_battery_voltage', ev3.get_battery_voltage()
	ev3.reset_motor_angle(port)		
	ev3.set_motor_direction(port, 1)
	ev3.set_motor_speed(port, 10)	
	ev3.motor_on(port)	
	for i in range(200):
		print 'motor a', ev3.get_motor_angle(1)
		print 'motor b', ev3.get_motor_angle(2)
		print 'motor c', ev3.get_motor_angle(4)
		print 'motor d', ev3.get_motor_angle(8)
		time.sleep(0.1)
		
	ev3.reset_motor_position(port)
	ev3.set_motor_direction(port, 1)
	ev3.set_motor_speed(port, 10)	
	ev3.motor_on(port)
	for i in range(50):
		#ev3.beep(freq=400+10*i, duration=200)
		#print 'light', ev3.read_light()
		time.sleep(0.1)
	ev3.set_motor_direction(port, -1)
	ev3.set_motor_speed(port, 50)
	ev3.motor_on(port)
		
	ev3.motor_off(port)	
	print ev3.get_motor_angle(port)
	ev3.disconnect()
	
if __name__ == "__main__":
	hostname = socket.gethostname().lower()		
	if hostname[-2] == '0': hostname = hostname[:-2] + hostname[-1]	
	try:
		hostname = sys.argv[1]
	except: pass
	print 'hostname', hostname
	sys.exit(main(hostname))