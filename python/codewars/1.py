try:
	line = int(raw_input(""))
	while(line):
		index = [line]
		x = line
		y = line
		sum = 0
		while(x+y>=3):
			x = line/3
			y = line%3
			#print x, y
			index.append(x)
			line = x+y
		for i in index:
			sum = sum + i
		print sum
		line = int(raw_input(""))
except:
	pass