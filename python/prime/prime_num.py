import math
data = open('prime.txt')
prime = [1,2,3]
data.write(prime)
for num in data:
	prime.append(num)
	



def isPrime(n):  
    if n <= 1:  
		return False 
    for i in range(2, int(math.sqrt(n)) + 1):  
		if n % i == 0:  
			return False 
    return True 

i = len(prime)

print prime
"""
while(1):
	if isPrime(i):
		prime.append(i)
		print prime[len(prime)-1]
	i+=1
"""