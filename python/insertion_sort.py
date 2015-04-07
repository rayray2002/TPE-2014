list = [1, 95, 73, 7, 673, 5, 62, 95, 51, 8, 62, 95]

for i in range(1, len(list)):
	temp = list[i]
	j = i
	while j > 0 and temp < list[j - 1]:
		list[j] = list[j - 1]
		j -= 1
	list[j] = temp
	
print list