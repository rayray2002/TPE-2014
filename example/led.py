import mraa
import time

laser = mraa.Gpio(13)
laser.dir(mraa.DIR_OUT)

while True:
	laser.write(1)
	time.sleep(0.1)
	laser.write(0)
	time.sleep(1.1)