# lecture 4
# file operation
import os

try:
	f = open("lecture.py")
	# f.readline() # line by line
	# print f.readlines() # read all materials at once
except IOError, e:
	print 'unable to open file'

import pickle

# stack1 = Stack()
# stack1.push(13)
# stack1.push(22)
# stack1.push(90)
# stack11.pop
# f = open('pickle1.py','w')
# pickle.dump([stack1],f)

# parent class
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

# subclass
class myAccount(Bank_Account):
	def __init__(self):
		self.balance = 500
		print 'my account is created: ' + str(self.balance)

print type(myAccount)
print issubclass(myAccount, Bank_Account)

account1 = myAccount()

# class as a dynamic record
class Empty(object):
	pass

myData = Empty()
myData.age = 22
myData.surname = 'Lam'
print myData.surname

# functional programming
def odd(number):
	return number%2==1
num = [1,2,3,4,5,6,7]
# use filter() to remove all number return FALSE from odd()
print filter(odd, num)