from wsgiref.simple_server import make_server
from cgi import parse_qs
#import mraa
import time
from uart import SerialManager

smgr = SerialManager('/dev/ttyMFD1')
smgr.start()

def my_app(environ, start_response):
	"""a simple led wsgi application"""
	def index():
		status = '200 OK'
		response_headers = [('Content-type', 'text/plain')]
		start_response(status, response_headers)
		return ["please enter xy"]
	p = environ['PATH_INFO']
	if p.find("/control")>=0:
		d = parse_qs(environ['QUERY_STRING'])
		state = d.get('state',[0])[0]
		
		smgr.write('a' + state + '\n')
		print repr(smgr.read())
			
	return index()

httpd = make_server('', 8000, my_app)
print "Serving on port 8000..."
httpd.serve_forever()
