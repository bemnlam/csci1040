import sys

line_count = 0
word_count = 0
char_count = 0
fname = ""

if len(sys.argv) >= 2:
	fname = sys.argv[1]
	# print 'fname= ' + fname

try:
	fp = open(fname, 'r')
	for line in fp.readlines():
		line_count += 1
		word_count += len(line.split())
		char_count += len(line)

	print 'Number of characters : ' + str(char_count)
	print 'Number of words : ' + str(word_count)
	print 'Number of lines : ' + str(line_count)

except IOError:
   print 'Opening filename does not exist!'
   exit(1)
