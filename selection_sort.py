list = [1, 45, 6, 38, 2, 8, 29, 60, 18, 35]
#answer[1, 2, 6, 8, 18, 29, 35, 38, 45, 60]

for i in range(len(list)):
	least = i
	for j in range(i + 1, len(list)):
		if list[j] < list[least]:
			least = j
			
	temp = list[least]
	list[least] = list[i]
	list[i] = temp
	
for k in range(len(list)):
	print list[k]