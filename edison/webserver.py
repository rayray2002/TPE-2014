from wsgiref.simple_server import make_server
import mraa

x = mraa.Gpio(13)
x.dir(mraa.DIR_OUT)
 
def on():
	print "on"
	x.write(1)
	
def off():
	print "off"
	x.write(0)

def my_app(environ, start_response):
	"""a simple wsgi application"""
	def ray():
		status = '200 OK'
		response_headers = [('Content-type', 'text/plain')]
		start_response(status, response_headers)
		return ["abc"]
		
	path = environ['PATH_INFO']
	if path.find("/on")>=0:
		on()
	elif path.find("/off")>=0:
		off()
	#print path
	return ray()

port = 8000

httpd = make_server('0.0.0.0', port, my_app)
print "Serving on port " + str(port)
httpd.serve_forever()