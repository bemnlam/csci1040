# part1 q2
def pow(a,n):
	if n == 0:
		return 1
	# even
	elif n%2 == 0:
		return pow(a*a, n/2)
	#odd
	elif n%2 == 1:
		return a * pow(a, n-1)
