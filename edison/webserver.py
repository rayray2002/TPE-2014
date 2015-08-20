from wsgiref.simple_server import make_server
import mraa
html = """<!DOCTYPE html>
<html>
<head>
    <script src="http://code.jquery.com/jquery-2.1.4.js"></script>
	<script type="text/javascript">
	console.log("hello world #1");
	</script>
</head>

<body>
<a><img id="switch" src="http://www.clker.com/cliparts/4/6/u/B/L/k/incandescent-light-bulb-off-hi.png"></a>
</body>


<script type="text/javascript">
function on() {
    console.log("on");
    flag = true;
    src = "http://www.clker.com/cliparts/c/B/T/E/V/y/incandescent-light-bulb-on-hi.png";
    $('#switch').attr("src", src);
    $.get( "/on" );
}

function off() {
    console.log("off");
    flag = false;
     src = "http://www.clker.com/cliparts/4/6/u/B/L/k/incandescent-light-bulb-off-hi.png";
    $('#switch').attr("src", src);
    $.get( "/off" );
}

var flag = false;

$( document ).ready(function() {
    console.log("hello world");
	$('#switch').click( function (e) {
      if( flag == true ) off();
      else on();
    });
});
</script>
  
</html>
"""

x = mraa.Gpio(13)
x.dir(mraa.DIR_OUT)
 
def on():
	print "on"
	x.write(1)
	
def off():
	print "off"
	x.write(0)

def my_app(environ, start_response):
	"""a simple led wsgi application"""
	def index():
		status = '200 OK'
		response_headers = [('Content-type', 'text/html')]
		start_response(status, response_headers)
		return html
		
	path = environ['PATH_INFO']
	if path.find("/on")>=0:
		on()
	elif path.find("/off")>=0:
		off()
	#print path
	return index()

port = 8000

httpd = make_server('0.0.0.0', port, my_app)
print "Serving on port " + str(port)
httpd.serve_forever()