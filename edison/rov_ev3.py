from uart import SerialManager

def run_proxy():
	#TODO: check EV1 S1 and S2 part
	proxy = SerialProxy('COM2', 'COM3')
	proxy.start()
	
	while True:
		time.sleep(1)
	
if __name__ == "__main__":
	run_proxy()