try:
	line = raw_input("")
	while(line):
		error = 0		
		index = []
		for l in line:
			index.append(l)
		if index[0] == 'A':
			index[0] = 1
		elif index[0] == 'E':
			index[0] = 9
		elif index[0] == 'P':
			index[0] = 17
		elif index[0] == 'M':
			index[0] = 25
		else:
			error = 1
		if error == 1:
			print "Fail"
			line = raw_input("")
			break
		sum = 0
		for i in range(7):
			sum += int(index[i+1])*(i+1)
		sum = (index[0]+sum)%10
		if (10-sum) == int(index[8]):
			print "Success"
		else:
			print "Fail"
		line = raw_input("")
except:
	pass