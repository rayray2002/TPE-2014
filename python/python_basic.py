import time
import calendar
#print
print "Hello, Python!"

#Variables
i = 1 #int
f = 1.5 #float
s = "ray" #string ""
s2 = 'ray' #string ''
a = [1,2,3,4,5] #array

print i
print f
print s
print s2
print a

#chinese
c = u'中文'
print c

#string
s = "Hello ray"
print s[0] #H
print s[3:7] #lo r
print s[3:] #lo ray

#array(can change)
a = [1,2,6,4,5,9,4,8,7,0]
print a[0] 
print a[3:7] 
print a[3:] 
print len(a)
a.append(10)
print a
a.pop(1)
print a
a.insert(1, 2)
print a
a.remove(5)
print a
a.reverse()
print a
a.sort()
#tuple(can't change)
t = (1,2,3,4,5,6,7,8,9,0)
print t[0] #1
print t[3:7] #4 5 6 7
print t[3:] #4 5 6 7 8 9 0

#dict
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

bigdict = {'name': 'ray','code':1234, 'car': 'BMW', 'time': '12:00'}

print dict['one']   
print dict[2]       
print bigdict          
print bigdict.keys()   
print bigdict.values()

#Operators
a = 3
b = 2
print a + b
print a - b
print a * b
print a / b

print a > b
print a < b
print a <= b
print a >= b
print a == b
print a != b

a += b #a = a + b
print a
a = 3
a -= b #a = a - b
print a

#logic
a = True
b = False
print a or b
print a and b
print a and a
print not a
#Decision
a = 5
if (a < 0):
	print "a > 0"
elif (a > 10):
	print "a > 10"
else:
	print "10 > a > 0"

#loop
i = 0
for i in range(10):
	print i
names = ['ray', 'eric', 'olivia', 'ariel']
for name in names:
	print name
i = 0
while (i < 5):
	print i
	i += 1

#string operators
a = "dog"
n = 5
print "it is a %s"%a
print "there are %d %s"%(n, a)

#time
localtime = time.localtime(time.time())
print "Local current time :", localtime
year = localtime[0]
month = localtime[1]
print year, month
localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime
cal = calendar.month(year, month)
print "Here is the calendar:"
print cal

#function
def printer(str):
	print str
	return
s = "ray"
printer(s)

#try except
def number_convert(var):
    u'轉換成數值'
    try:
       return int(var)
    except ValueError, e:
       print u"傳入不是個數值 錯誤是: ", e

number_convert("123");
number_convert("ray");

#class
class Student:
   def __init__(self, name, grade):
      self.name = name
      self.grade = grade
   
   def displayEmployee(self):
      print "Name : ", self.name,  ", Grade: ", self.grade

s1 = Student("Eric", 8)
print s1.name, s1.grade
s2 = Student("Ray", 6)
print s2.name, s2.grade