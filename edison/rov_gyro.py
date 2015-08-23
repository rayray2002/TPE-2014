from uart import SerialManager
import struct
import time


smgr = SerialManager('COM12')
smgr.read_num_bytes = 8
smgr.baudrate = 9600
smgr.start()

print '#1'

while True:
	data = smgr.read()
	if data:
		for d in data:
			if len(d) == 7:
				x, y, z = struct.unpack('<xhhh', d)
				print x/100.0, y/100.0, z/100.0
	time.sleep(0.1)