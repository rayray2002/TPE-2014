from wsgiref.simple_server import make_server
from cgi import parse_qs
#import mraa
import time
from uart import SerialManager
import serial

smgr = None
try:
	smgr = SerialManager('/dev/ttyMFD1')
	smgr.start()
except serial.serialutil.SerialException:
	pass
	
html = """
<html>
<head>
    <script src="http://code.jquery.com/jquery-2.1.4.js"></script>
	<script type="text/javascript">
	console.log("hello world #1");
	</script>
</head>

<body>
<b id="forward">Forward </b> <br>
<b id="backward">Backward </b> <br>
<b id="right">Right </b> <br>
<b id="left">Left </b> <br>
<b id="up">Up </b> <br>
<b id="down">Down </b> <br>
<b id="fast">Fast </b> <br>
<b id="slow">Slow </b> <br>
<b id="stop">Stop </b> <br>
</body>


<script type="text/javascript">
function forward() {
    console.log("forward");
    $.get( "/control?state=f" );
}

function backward() {
    console.log("backward");
    $.get( "/control?state=b" );
}

function stop() {
    console.log("stop");
    $.get( "/control?state=s" );
}

function right() {
    console.log("right");
    $.get( "/control?state=r" );
}

function left() {
    console.log("left");
    $.get( "/control?state=l" );
}

function up() {
    console.log("up");
    $.get( "/control?state=u" );
}

function down() {
    console.log("down");
    $.get( "/control?state=d" );
}

function fast() {
    console.log("fast");
    $.get( "/control?state=1" );
}

function slow() {
    console.log("slow");
    $.get( "/control?state=2" );
}

$( document ).ready(function() {
    console.log("hello world");
	$('#forward').click( function (e) {
        forward()
    });
    
    $('#backward').click( function (e) {
        backward()
    });
    
    $('#stop').click( function (e) {
        stop()
    });
    
    $('#up').click( function (e) {
        up()
    });
    
    $('#down').click( function (e) {
        down()
    });
    
    $('#right').click( function (e) {
        right()
    });
    
    $('#left').click( function (e) {
        left()
    });
    
    $('#fast').click( function (e) {
        fast()
    });
    
    $('#slow').click( function (e) {
        slow()
    });
});
</script>
  
</html>
"""
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
		print 'state', state
		
		if smgr:
			smgr.write('a' + state + '\n')
			print repr(smgr.read()) 
		start_response('200 OK', [('Content-type', 'text/html')])
		return ""
		
	elif p.find("/js") >= 0:
		content = open('./js/' + p.split('/')[-1] ).read()
		start_response('200 OK', [('Content-type', 'text/javascript')])
		return content
		
	elif p.find("/css") >= 0:
		content = open('./css/' + p.split('/')[-1] ).read()
		start_response('200 OK', [('Content-type', 'text/css')])
		return content
		
	elif p.find("/images") >= 0:
		content = open('./images/' + p.split('/')[-1], 'rb' ).read()
		start_response('200 OK', [('Content-type', 'image/png')])
		return content
		
	else:	
		return index()

httpd = make_server('', 8000, my_app)
print "Serving on port 8000..."
httpd.serve_forever()
