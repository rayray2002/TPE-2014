import itertools

num = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9], 10))

for n in num:
	a = n[0]*100+n[1]*10+n[2]
	b = n[3]*100+n[4]*10+n[5]
	c = n[6]*1000+n[7]*100+n[8]*10+n[9]
	if a * b == c:
		print a,b,c