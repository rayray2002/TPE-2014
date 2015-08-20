# -*- coding: utf-8 -*-

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
import time, random
import ev3_brick
from threading import Thread
import signal
import sys, traceback
from datetime import datetime

# see this: https://wiki.qut.edu.au/display/cyphy/Mailbox+and+Messages

ev3 = ev3_brick.EV3Brick()	
ev3.connect('smart3')	
time.sleep(3)
print 'ev3.state', ev3.state
print 'reciving...'
for i in range(30):
	c = ev3.socket.recv(1)	
	print repr(c)
print("write message")
ev3.write_message('abc', 'hello!')
time.sleep(10)