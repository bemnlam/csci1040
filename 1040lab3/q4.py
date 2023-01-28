def quicksort(a):
	if a == []:
		return []
	else:
		pivot = a[0]
		smaller = quicksort([x for x in a[1:] if x < pivot])
		bigger = quicksort([x for x in a[1:] if x > pivot])
		return smaller + [pivot] + bigger

# from random import shuffle
# a = range(1,11)
# shuffle(a)
# print a

# a = quicksort(a)
# print a