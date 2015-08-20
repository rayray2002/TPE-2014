from __future__ import division
from sympy import *
import itertools
import time

start = time.clock()
num = ['1','2','3','4','5','6','7','8','9']
data = list(itertools.product(['+','-',''], repeat=len(num)))
calc = []
run = '1'

for d in data:
	#print run
	expr = sympify(run)
	if expr == 100:
		calc.append(run)
	run = ''
	for c in range(len(d)):
		run = run + d[c] + num[c]

for c in calc:
	print c
	
print time.clock()-start