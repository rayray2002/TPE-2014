import urllib2
# -*- coding: utf8 -*-

url = 'http://www.cwb.gov.tw/rss/forecast/36_01.xml'

f = urllib2.urlopen(url)
body = f.read()
lines = body[body.find('<item>'):]
line = lines[lines.find('CDATA[') + 7:lines.find(']')]
#w = line.decode('utf8')
print line