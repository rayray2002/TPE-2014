#do
 # swapped = false
  #for i = 1 to numOfElements exclusive
  #  if leftElement > rightElement
  #    swap(leftElement, rightElement)
   #   swapped = true
#while swapped

#shuffle

list = [1, 29, 3, 84, 72, 75, 62, 93]

while True:
	swapped = False
 	for i in range(len(list) - 1):
		if list[i] > list[i + 1] :
			temp = list[i + 1]
			list[i + 1] = list[i]
			list[i] = temp
			swapped = True
	if(swapped == False):
		break
		
for i in range(len(list)):
	print list[i]