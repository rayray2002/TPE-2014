#!/usr/bin/python
import serial
import threading
import time
from threading import Thread
from uart import SerialManager


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
			print '#1', count
			s1.write( str(count) )
			data = s1.read()
			if data: print(repr(data))
			time.sleep(0.5)
	except KeyboardInterrupt:
		s1.close()
	finally:
		s1.close()
	s1.join()

if __name__ == "__main__":
	test_serial() 