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
		
	def read(self, start_token='a', end_token = '\n'):
		ret = []
		if self.read_flag:
			while True:
				spos = epos = 0
				if start_token:
					spos = self.read_buffer.find(start_token)
					if spos<0: spos = 0
				if end_token:
					epos = self.read_buffer.find(end_token, spos)
				if epos > spos:
					data = self.read_buffer[spos:epos]
					self.read_buffer = self.read_buffer[epos:]
					ret.append( data )
				else: break
			self.read_flag = False
		return ret
		
	def write(self, data):
		self.out_queue.put( data )
		
	def run(self):
		try:
			while self.running:
				if self.sleeptime: time.sleep(self.sleeptime)
				in_data = self.ser.read(self.read_num_bytes)
				if in_data:
					self.read_buffer += in_data
					self.read_flag = True
				try:
					out_buffer = self.out_queue.get_nowait()
					self.ser.write(out_buffer)
				except Empty:
					pass
		except (KeyboardInterrupt, SystemExit): pass
		self.ser.close()
		
	def close(self):
		self.running = False
	

def main():
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
			print '#1', count
			s1.write( str(count) )
			data = s1.read()
			print(repr(data))
	except KeyboardInterrupt:
		s1.close()
	finally:
		s1.close()
	s1.join()

if __name__ == "__main__":
	main() 
