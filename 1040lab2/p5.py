class Rectangle(object):
	def __init__(self, userw, userh):
		self.w = userw
		self.h = userh
	# getter
	def height(self):
		return self.h
	def width(self):
		return self.w
	#methods
	def area(self):
		return self.w *self.h
	def perimeter(self):
		return 2 * (self.w + self.h)
	def isSquare(self):
		return (self.w == self.h)
