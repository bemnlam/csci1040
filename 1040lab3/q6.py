# Stack
class Stack(object):
	def __init__(self):
		self.storage = []
	def push(self, newValue):
		self.storage.append(newValue)
	def top(self):
		return self.storage[len(self.storage)-1]
	def pop(self):
		result = self.top()
		self.storage.pop()
		return result
	def isEmpty(self):
		return len(self.storage) == 0

# Engine
class CalculatorEngine(object):
	def __init__(self):
		self.dataStack = Stack()

	def pushOperand(self, value):
		self.dataStack.push(value)

	def currentOperand(self):
		return self.dataStack.top()

	def performBinary(self, fun):
		right = self.dataStack.pop()
		left = self.dataStack.top() #should be pop()
		self.dataStack.push(fun(left,right))

	def doAddition(self):
		self.performBinary(lambda x,y: x+y)

	def doSubtraction(self):
		self.performBinary(lambda x,y: x-y)

	def doMultiplication(self):
		self.performBinary(lambda x,y: x*y)

	def doDivision(self):
		self.performBinary(lambda x,y: x/y)

	def doTextOp(self, op):
		if 	(op == '+'): self.doAddition()
		if 	(op == '-'): self.doSubtraction()
		if 	(op == '*'): self.doMultiplication()
		if 	(op == '/'): self.doDivision()

# Calculator
class RPNCalculator(object):
	def __init__(self):
		self.calcEngine = CalculatorEngine()
	def eval(self, line):
		words = line.split(" ")
		for item in words:
			if item in '+-*/':
				self.calcEngine.doTextOp(item)
			# modulo operation
			elif item in '%':
				self.calcEngine.performBinary(lambda x,y: x%y)
			else:
				self.calcEngine.pushOperand(int(item))
		return self.calcEngine.currentOperand()
	def run(self):
		while True:
			line = raw_input("type an expression: ")
			if len(line) == 0:
				break
			# exception handling
			try:
				print self.eval(line)
			except ZeroDivisionError:
				print('division by zero')
			except ValueError:
				print('numeric and "+-*/" only')
			except:
				print('a message')

calc = RPNCalculator()
calc.run()
