import sys
# 1a
str = 	raw_input("enter the string  : ")
fname = raw_input("enter the filename: ")
try:
	fp = open(fname, 'r')
	for line in fp.readlines():
		if str in line:
			sys.stdout.write(line)
except:
   print 'Opening filename does not exist!'
   exit(1)
