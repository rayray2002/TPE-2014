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
		
	def run(self):
		try:
			while self.running:
				if self.sleeptime: time.sleep(self.sleeptime)
				in_data = self.ser.read(self.read_num_bytes)
				print 'run in_data', in_data
				if in_data:
					self.in_queue.put(in_data)
				try:
					out_buffer = self.out_queue.get_nowait()
					self.ser.write(out_buffer)
				except Empty:
					pass
		except (KeyboardInterrupt, SystemExit): pass
		self.ser.close()
		
	def read(self):
		return self.in_queue.get()
		
	def write(self, data):
		self.out_queue.put( data )
		
	def close(self):
		self.running = False
	
