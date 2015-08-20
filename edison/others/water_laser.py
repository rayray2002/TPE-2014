from wsgiref.simple_server import make_server
from cgi import parse_qs
import mraa
import time

def my_app(environ, start_response):
	"""a simple led wsgi application"""
	def index():
		status = '200 OK'
		response_headers = [('Content-type', 'text/plain')]
		start_response(status, response_headers)
		return ["please enter xy"]
		
	def getbit(data, bit):
		return (data & (1<<(7 - bit))) >> 7 - bit
		
	def cord(query_dict, start_response):
		x = int(query_dict.get('x',[0])[0])
		y = int(query_dict.get('y',[0])[0])
		data = [x, y]
		print 'cord', x, y
		laser_pin = mraa.Gpio(8)
		laser_pin.dir(mraa.DIR_OUT)
		delay = 0.3 #0.3 * 17 + 2
		for i in range(5):
			print '='*10, i
			print "start bit"
			laser_pin.write(1)
			time.sleep(delay/3)
			laser_pin.write(0)
			time.sleep(delay*2/3)
			
			for l in range(len(data)):
				if l == 0: print "x"
				else: print "y"
				
				for i in range(8):
					if getbit(data[l],i) == 1:
						print i, "on"
						laser_pin.write(1)
					else:
						print i, "off"
						laser_pin.write(0)
					time.sleep(delay/3)
					laser_pin.write(0)
					time.sleep(delay*2/3)

			time.sleep(2)
		
		status = '200 OK'
		response_headers = [('Content-type', 'text/plain')]
		start_response(status, response_headers)
		return "Sent"
		
	# http://192.168.1.109:8123/motor?
	def motor(environ, start_response):
		dir = int(query_dict.get('dir',[0])[0]) #either 1 or 2
		t = int(query_dict.get('time',[0])[0])
		p = int(query_dict.get('pwm',[0])[0])
		in_1 = mraa.Gpio(5) #arduino 5
		in_1.dir(mraa.DIR_OUT)
		in_2 = mraa.Gpio(4) #arduino 4
		in_2.dir(mraa.DIR_OUT)
		standy_pin = mraa.Gpio(6) #arduino 6
		standy_pin.dir(mraa.DIR_OUT)
		pwm = mraa.Pwm(3) #arduino 3
		pwm.enable(True)
		#print p
		if p == 0:
			PWM = 0.35
		else:
			PWM = p/142.85
		pwm.write(PWM)
		
		standy_pin.write(1) #disable standby
		if dir==1:
			in_1.write(1)
			in_2.write(0)
		else:
			in_1.write(0)
			in_2.write(1)
		pwm.write(PWM)
		time.sleep(t)
		standy_pin.write(0) #standby
		
		status = '200 OK'
		response_headers = [('Content-type', 'text/plain')]
		start_response(status, response_headers)
		return "Sent"

	p = environ['PATH_INFO']
	query_dict = parse_qs(environ['QUERY_STRING'])
	
	if p.find("/cord")>=0:
		return cord(query_dict, start_response)
		
	elif p.find("/motor")>=0:
		return motor(query_dict, start_response)
	elif p.find("/")>=0:
		return index()
		

httpd = make_server('', 8123, my_app)
print "Serving on port 8123..."
httpd.serve_forever()