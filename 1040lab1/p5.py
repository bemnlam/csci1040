# Bonus
user_input = raw_input("Enter your sentence:\n")
reverse_input = str(user_input)[::-1]

if user_input == reverse_input:
	print 'YES'
else:
	print 'NO'