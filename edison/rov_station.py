from wsgiref.simple_server import make_server
from cgi import parse_qs
#import mraa
import time
from uart import SerialManager
import serial
import json
import threading
import struct


import socket
host = socket.gethostname()

device_status = {}
device_status['pitch'] = 0
device_status['roll'] = 0
device_status['yaw'] = 0
device_status['light'] = 0
device_status['camera'] = 0

smgr = None
try:
	if host.lower().find('edison')>=0:
		smgr = SerialManager('/dev/ttyMFD1')
	if host.lower().find('eric')>=0:
		smgr = SerialManager('COM12')
	smgr.start()
except serial.serialutil.SerialException, e:
	print type(e), e

def my_app(environ, start_response):
	"""a simple led wsgi application"""
	def index():
		status = '200 OK'
		response_headers = [('Content-type', 'text/html')]
		html = open('remote.html').read()
		start_response(status, response_headers)
		return html
		
	p = environ['PATH_INFO']
	print 'path', p
	
	if p.find("/control")>=0:
		d = parse_qs(environ['QUERY_STRING'])
		state = d.get('state',[0])[0]
		arg = d.get('arg',[0])[0]
		print 'state', state, 'arg', arg
		
		if state == 'light_on':
			device_status['light'] = 1
		elif state == 'light_off':
			device_status['light'] = 0
		elif state == 'camera_on':
			device_status['camera'] = 1
		elif state == 'camera_off':
			device_status['camera'] = 0

		if smgr:
			if arg:
				smgr.write('a' + state + '/' + arg + '\n')
			else:
				smgr.write('a' + state + '\n')
			print repr(smgr.read()) 
		start_response('200 OK', [('Content-type', 'text/html')])
		return ""
		
	elif p.find("/poll") >= 0:
		global device_status
		start_response('200 OK', [('Content-type', 'application/json')])
		ret  = json.dumps(device_status)
		return ret
		
	elif p.find("/js") >= 0:
		content = open('./js/' + p.split('/')[-1] ).read()
		start_response('200 OK', [('Content-type', 'text/javascript')])
		return content
		
	elif p.find("/css") >= 0:
		content = open('./css/' + p.split('/')[-1] ).read()
		start_response('200 OK', [('Content-type',	 'text/css')])
		return content
		
	elif p.find("/images") >= 0:
		content = open('./images/' + p.split('/')[-1], 'rb' ).read()
		start_response('200 OK', [('Content-type', 'image/png')])
		return content
	else:	
		return index()

poll_flag = True;
def poll_status_forever():
	data = None
	
	while poll_flag:
		data = smgr.read()
		if data:
			for d in data:
				if len(d) == 6:
					x, y, z = struct.unpack('<hhh', d)
					if x!=0:
						#print x/100.0, y/100.0, z/100.0
						device_status['pitch'] = x/100.0
						device_status['roll'] = y/100.0
						device_status['yaw'] = z/100.0
		time.sleep(0.2)
		
t = threading.Thread(target = poll_status_forever)
t.start()

try:
	httpd = make_server('', 8000, my_app)
	print "Serving on port 8000..."
	httpd.serve_forever()
except KeyboardInterrupt:
	pass
	
print 'exiting...'
poll_flag = False
if smgr: smgr.close()
