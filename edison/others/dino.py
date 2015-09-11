from wsgiref.simple_server import make_server
from cgi import parse_qs
import mraa
import time
html = """<!DOCTYPE html>
<html>
<head>
    <script src="http://code.jquery.com/jquery-2.1.4.js"></script>
	<script type="text/javascript">
	console.log("hello world #1");
	</script>
</head>

<body>
<a><img id="switch" src="http://images.clipartpanda.com/t-rex-dinosaur-clip-art-T-Rex-Dinosaur_1.png"></a>
</body>


<script type="text/javascript">
function on() {
    console.log("on");
    flag = true;
    src = "http://img1.wikia.nocookie.net/__cb20140227230627/dinosaurs/images/c/c9/Ls_shutterstock_105146921_free.jpg";
    $('#switch').attr("src", src);
    $.get( "/motor?dir=1&time=1&pwm=100" );
}

function off() {
    console.log("off");
    flag = false;
     src = "http://images.clipartpanda.com/t-rex-dinosaur-clip-art-T-Rex-Dinosaur_1.png";
    $('#switch').attr("src", src);
    $.get( "/motor?dir=2&time=1&pwm=100" );
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
def my_app(environ, start_response):
	"""a simple led wsgi application"""
	def index():
		status = '200 OK'
		response_headers = [('Content-type', 'text/plain')]
		start_response(status, response_headers)
		return ["please enter path"]

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
		response_headers = [('Content-type', 'text/html')]
		start_response(status, response_headers)
		return html

	p = environ['PATH_INFO']
	query_dict = parse_qs(environ['QUERY_STRING'])
		 
	elif p.find("/motor")>=0:
		return motor(query_dict, start_response)
		
	elif p.find("/")>=0:
		return index()
		

httpd = make_server('', 8123, my_app)
print "Serving on port 8123..."
httpd.serve_forever()