# lecture 1
# to concat a string and a number, the number need to be using str()
v = 5
print str(v) + ": hello, world"

# multiple assignment
a, b = 0, 1
while b < 10:
	print b
	a, b = b, a+b
print 'End'
print '-'*80
#
# lecture 2: stirng, list, function, classes
print 'doesn\'t'
# string cannot be modified once it is created (just like C)
word = "python "
print '[' + word *3 + ']'
# from word[0] to word[2-1]
print word[0:2]
print word[:4]
# from word[3] to the end of stirng
print word[3:]
# -ve position means from right to left
print word[:-2]
# function declaration
def area_of_rect(w, h):
	return w * h
print area_of_rect(2,3)
print area_of_rect("python!",3)
# but, string cannot multiply with a float!
# another function
def ask_lunch(prompt, set="none"):
	choice = raw_input(prompt)
	if choice == '':
		return set
	else:
		return choice
# print ask_lunch("what would you like? ")
# raw_input() prompt is the message you want to show and the return value is the user input
# declare global variable
global b
b = 10
print b
# function pointer
def fun(a):
	print 'argv is ' + a
another_fun = fun
another_fun("using function pointer!")
def min_and_max(info):
	return (min(info), max(info))
tp1 = (x,y) = min_and_max("hello")
print tp1
# no multiple inhert
class Bank_Account(object):
	def __init__(self):
		self.balance = 0
	def deposit(self, amount):
		self.balance += amount
		return self.balance
	def withdraw(self, amount):
		self.balance -= amount
		return self.balance
	def show(self):
		return self.balance
print Bank_Account.__name__
# to get the substr with gap
lang = "Python!"
print lang[0:7:3]
# to reverse substr with gap
print lang[::-2]
print '-'*80
word = "hello, world"
print '{0} is {1}!'.format("python", "2.7")
b = 1
while b < 3:
	print word[b]
	b = b+1
print '-'*80
#
# lecture 3
# Dictionary / hashes / map / associate array
dict = { }
dict['name'] = 'Donald Duck'
dict['age'] = 63
dict['eyes'] = 'black'
print dict
del dict['name']
# multiple ingert
class A(object):
	def doa(self):
		print "class A"
class B(object):
	def dob(self):
		print "class B"
class C(A,B):
	def doc(self):
		print "class C"
v = C()
v.doc()
#
