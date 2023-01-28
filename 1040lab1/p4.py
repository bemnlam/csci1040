# Problem 1
from random import *
# gen a ramdon no
comp_num =randint(1, 10)
# user guess
while True:
	user_num = input('Please input your guess\n')
	if user_num == comp_num :
		print 'You are right'
		break
	elif user_num > comp_num :
		print 'Too high!'
	else:
		print 'Too low!'
