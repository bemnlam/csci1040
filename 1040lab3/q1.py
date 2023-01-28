def unique1(lst):
	tmp = []
	for x in lst:
		if not x in tmp:
			tmp.append(x)
	return tmp
