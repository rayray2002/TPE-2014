# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
html = urllib.urlopen("http://python-data.dr-chuck.net/comments_256397.html").read()

soup = BeautifulSoup(html)

count = 0
sum = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
	count += 1
	num = int(tag.contents[0])
	#print num
	sum += num
	
print 'count:',count
print 'sum:' , sum