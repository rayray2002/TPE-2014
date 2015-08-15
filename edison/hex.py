#import mraa
import time
 
#x = mraa.Gpio(13)
#x.dir(mraa.DIR_OUT)
data = [0x55, 0xaa, 0xff, 0x88]

def getbit(data, bit):
	return (data & (1<<bit)) >> bit
	
while True:
	for l in range(len(data)):
		print "byte", l
		for i in range(8):
			if getbit(data[l],i) == 1:
				print "on"
				#x.write(1)
			else:
				print "off"
				#x.write(0)
			time.sleep(1)