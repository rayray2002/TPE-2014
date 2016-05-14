import sys

def num_():
	try:
		line = raw_input("")
		while(line):
			items = line.split()

			line = raw_input("")
	except EOFError:
		pass

if __name__ == "__main__":
	num_()