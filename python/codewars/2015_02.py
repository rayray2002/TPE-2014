try:
	line = int(raw_input(""))
	while(line):
		letter_array = ["H", "I", "J", "K", "L", "A", "B", "C", "D", "E", "f", "G"]
		num_array = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
		index = line-2015
		num = num_array[index%10]
		letter = letter_array[index%12]
		print num + letter
		line = int(raw_input(""))
except:
	pass