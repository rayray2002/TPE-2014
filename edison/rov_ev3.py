from uart import SerialManager
import socket
host = socket.gethostname()


def run_proxy():
	proxy = None
	if host.find('ev3') >= 0:
		proxy = SerialProxy('tty_in1', 'tty_in2')
	else: proxy = SerialProxy('COM2', 'COM3')
	proxy.start()
	
	while True:
		time.sleep(1)
	
if __name__ == "__main__":
	run_proxy()