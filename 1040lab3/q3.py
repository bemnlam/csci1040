# make a list
a = range(1,11)
# list b will store the result
b = []

# part a
def square(n):
	return n*n
def addone(n):
	return n+1

# (I)	produce square
b = map(square, a)
print b
# (II)	add 1 to original
b = map(addone, a)
print b

#####################
# part b
def le5(n):
	return n<=5
def evenSq(n):
	return (n*n)%2==0

# (I)	less than or eq. 5
b = filter(le5, a)
print b
#(II)	square is even
b = filter(evenSq, a)
print b