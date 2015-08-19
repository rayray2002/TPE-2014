#!/usr/bin/python
import serial
import threading
import time
from threading import Thread
from multiprocessing import Process, Queue
try:
    from queue import Empty
except ImportError:
    from Queue import Empty
	
	
class SerialManager(Thread):
	def __init__(self, device):
		super(SerialManager, self).__init__()
		self.ser = serial.Serial(device, baudrate=9600, bytesize=serial.EIGHTBITS,
			parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=0.1, 
			xonxoff=False, rtscts=False, writeTimeout=None)
		self.in_queue = Queue()
		self.out_queue = Queue()
		self.running = True # A flag to indicate thread shutdown
		self.read_num_bytes  = 256
		self.sleeptime = None
		self._chunker = None
		
	def read(self):
		return self.in_queue.get()
		
	def write(self, data):
		self.out_queue.put( data )
		
	def run(self):
		try:
			while self.running:
				if self.sleeptime: time.sleep(self.sleeptime)
				in_data = self.ser.read(self.read_num_bytes)
				print 'run in_data', in_data
				if in_data:
					write(in_data)
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