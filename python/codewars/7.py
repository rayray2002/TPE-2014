import sys, re

def num_7():
	try:
		line = raw_input("")
		while(line):
			items = line.split()
			answer = items[0]
			guess = items[1]
			
			a = b = 0

			for i in range(len(answer)):
				if answer[i] == guess[i]:
					a+=1
				for j in range(len(answer)):
					if answer[i] == guess[j]:
						b+=1
			print str(a)+'A'+str(b-a)+'B'
			
			line = raw_input("")
	except EOFError:
		pass

if __name__ == "__main__":
	num_7()