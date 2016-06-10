# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/known_by_Greg.html"
for i in range(7):
	#global url
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

	# Retrieve all of the anchor tags
	tags = soup('a')
	#print  tags

	url = tags[17].get('href', None)
print url