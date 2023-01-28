# a
def diff(first, second):
	tmp = []
	for x in first:
		if not x in second:
			tmp.append(x)
	return tmp

#print diff([1,3,4,7,8], [2,6,3,7,1])

# b
def union(first, second):
	return (second + diff(first, second))

#print union([1,3,4,7,8], [7,6,3,7,1])