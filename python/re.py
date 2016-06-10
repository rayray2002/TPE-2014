import re
text = open('regex_sum_256392.txt')
sum = 0
for line in text:
	nums = re.findall('[0-9]+',line)
	for num in nums:
		global sum
		sum += int(num)
		
print sum