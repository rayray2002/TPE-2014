import itertools
import time

start = time.clock()
num = [1,2,3,4,5,6,7,8,9]
data = list(itertools.product([0,1,2], repeat=len(num)))
term = 100
out = []

for i in range(len(data)):
	calc = [0]
	#print data[i]
	for j in range(len(num)):
		mode = (data[i])[j]
		last = calc[len(calc)-1]
		if mode == 0:
			if last == '+' or last == '-' or last == 0:
				calc[len(calc)-1] = num[j]
			else:
				if j != 0:
					calc.append(last*10 + num[j])
					calc.remove(calc[len(calc)-2])
				
		if mode == 1:
			if calc[0] == 0:
				calc[0] = (num[j])
			else:
				calc.append('+')
				calc.append(num[j])
				
		if mode == 2:
			if calc[0] == 0:
				calc[0] = '-'
				calc.append(num[j])
			else:
				calc.append('-')
				calc.append(num[j])
	#print calc
	if calc[0] == '-':
		ans = calc[1]*-1
	else:
		ans = calc[0]
	for c in range(len(calc)):
		if c != len(calc) and c != 0:
			if calc[c]  == '+':
				ans = ans + calc[c+1]
			if calc[c]  == '-':
				ans = ans - calc[c+1]
	#print ans
	if ans == term:
		string = ' '
		for s in calc:
			string = string + str(s)
		out.append(string)
		
for o in out:
	print o
	
print time.clock()-start