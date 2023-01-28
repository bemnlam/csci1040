
class Box(object):
	def __init__(self, ival):
		self.value = ival
# a
	def __cmp__(self, other):
		if self.value == other.value:
			return 0
		elif self.value > other.value:
			return 1
		else:
			return -1

# b
	def __add__(self, other):
		return Box(self.value+other.value)

# b1 = Box(10)
# b2 = Box(10)
# print b1<>b2

# b3 = b1+b2
# print b3.value