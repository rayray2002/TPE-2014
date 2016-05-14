import math
try:
	line = raw_input("")
	while(line):
		index = []
		for l in line:
			index.append(l)
		#print index
		for i in range(4):
			index.remove('(')
			index.remove(')')
			index.remove(',')
		for i in range(3):
			index.remove(' ')
		#print index
		for i in range(8):
			index[i] = int(index[i])
		#print index
		sides = [0,0,0]
		sides[0] = [math.hypot(index[0]-index[2],index[1]-index[3])]
		sides[1] = [math.hypot(index[4]-index[2],index[5]-index[3])]
		sides[2] = [math.hypot(index[0]-index[4],index[1]-index[5])]
		sides.sort()
		#print (sides[0])[0]+(sides[1])[0]
		if (sides[0])[0]+(sides[1])[0]<=(sides[2])[0]:
			print "Triangle doesn't exist."
			line = raw_input("")
			break
		#print sides
		line = raw_input("")
except NameError:
	print NameError