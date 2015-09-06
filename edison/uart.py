#!/usr/bin/python
import serial
import threading
import time
from threading import Thread
from multiprocessing import Process, Queue
try:
    from queue import Empty, Full
except ImportError:
    from Queue import Empty, Full
	


class SerialManager(Thread):
	def __init__(self, device):
		super(SerialManager, self).__init__()
		self.start_token = 'a'
		self.end_token = '\n'
		self.baudrate = 38400
		self.in_queue = Queue()
		self.out_queue = Queue()
		self.running = True # A flag to indicate thread shutdown
		self.read_num_bytes  = 128
		self.sleeptime = 0.01
		self.ser = serial.Serial(device, baudrate=self.baudrate,
			bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=0.2, xonxoff=False, rtscts=False, writeTimeout=None)
		self.read_buffer = ''
		self.read_flag = False
		
	def read(self):
		ret = []
		if self.read_flag:
			while True:
				spos = epos = 0
				spos = self.read_buffer.find(self.start_token)
				if spos<0: spos = 0
				epos = self.read_buffer.find(self.end_token, spos)
				if epos > spos:
					data = self.read_buffer[spos:epos]
					self.read_buffer = self.read_buffer[epos:]
					if data.endswith(self.end_token): data = data[:-1]
					if data.startswith(self.start_token): data = data[1:]
					ret.append( data )
				else: break
			self.read_flag = False
		return ret
		
	def write(self, data):
		print type(data), data
		self.out_queue.put( self.start_token + data + self.end_token )
		
	def run(self):
		try:
			while self.running:
				if self.sleeptime: time.sleep(self.sleeptime)
				in_data = self.ser.read(self.read_num_bytes)
				if in_data:
					#print 'rx', len(self.read_buffer)
					self.read_buffer += in_data
					self.read_flag = True
				try:
					#print 'tx'
					out_buffer = self.out_queue.get_nowait()
					self.ser.write(out_buffer)
				except Empty, e:
					pass
					#print type(e), e	
		except (KeyboardInterrupt, SystemExit): pass
		self.ser.close()
		
	def close(self):
		self.running = False
		
class SerialProxy(Thread):
	def __init__(self, device1, device2):
		super(SerialProxy, self).__init__()
		self.running = True
		self.managers = [] 
		self.managers.append( SerialManager(device1) )
		self.managers.append( SerialManager(device2) )
		self.sleeptime = 0.01
		for m in self.managers: m.start()
		
	def run(self):
		try:
			while self.running:
				if self.sleeptime: time.sleep(self.sleeptime)
				datas = self.managers[0].read()
				if datas:
					for data in datas:
						print 'data0', type(data), data
						self.managers[1].write(data)
				datas = self.managers[1].read()
				if datas:
					for data in datas:
						print 'data1', type(data), data
						self.managers[0].write(data)
		except (KeyboardInterrupt, SystemExit): pass
		self.close()
		
	def close(self):
		for s in self.managers:
			s.close()
		self.running = False
	

def test_proxy():
	proxy = SerialProxy('COM2', 'COM3')
	proxy.start()
	time.sleep(100000)
	
	
def test_serial():
	import argparse
	parser = argparse.ArgumentParser(description='A class to manage reading and writing from and to a serial port.')
	parser.add_argument('device', help='The serial port to use (COM4, /dev/ttyUSB1 or similar).')
	args = parser.parse_args()

	s1 = SerialManager(args.device)
	s1.sleeptime = 0.01
	s1.read_num_size = 512
	s1.start()

	count = 0
	try:
		while True:
			count += 1
			#print '#1', count
			s1.write( str(count) )
			data = s1.read()
			#print(repr(data))
			time.sleep(0.5)
	except KeyboardInterrupt:
		s1.close()
	finally:
		s1.close()
	s1.join()

if __name__ == "__main__":
	test_proxy() 
