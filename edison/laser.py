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
	
	p = environ['PATH_INFO']
	if p.find("/cord")>=0:
		d = parse_qs(environ['QUERY_STRING'])
		
		x = int(d.get('x',[0])[0])
		y = int(d.get('y',[0])[0])
		data = [x, y]
		print x, y
		
		laser_pin = mraa.Gpio(8)
		laser_pin.dir(mraa.DIR_OUT)
		delay = 1
		for i in range(100):
			print '='*10, i
			print "start bit"
			laser_pin.write(1)
			time.sleep(delay/2)
			laser_pin.write(0)
			time.sleep(delay/2)
			
			for l in range(len(data)):
				if l == 0:
					print "x"
				else:
					print "y"
				for i in range(8):
					if getbit(data[l],i) == 1:
						print "on"
						laser_pin.write(1)
					else:
						print "off"
						laser_pin.write(0)
					time.sleep(delay/2)
					laser_pin.write(0)
					time.sleep(delay/2)
					
			time.sleep(3)
		
	return index()

httpd = make_server('', 8000, my_app)
print "Serving on port 8000..."
httpd.serve_forever()