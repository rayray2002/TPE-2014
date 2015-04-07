
s = 75
j = 1

#set bit
def set_bit(bit):
	global s, j 
	print hex(s | j << bit)
 	
def check_bit(bit):
	global s, j 
	print (s & j << bit)
	
def toggle_bit(bit):
	global s, j
	print (s ^ j << bit)

def clear_bit(bit):
	global s, j 
	j = j << bit
	print (s & ~j)
#set bit
set_bit(2)

#check bit
check_bit(2)

#toggle 0->1, 1->0
toggle_bit(2)

#clear
clear_bit(2)