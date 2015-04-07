list = [1, 45, 6, 38, 2, 8, 29, 60, 18, 35]
answer = [1, 2, 6, 8, 18, 29, 35, 38, 45, 60]

def selection_sort(data):
	for i in range(len(data)):
		least = i
		for j in range(i + 1, len(data)):
			if data[j] < data[least]:
				least = j
				
		temp = data[least]
		data[least] = data[i]
		data[i] = temp

	return data


assert(selection_sort(list) == answer)
