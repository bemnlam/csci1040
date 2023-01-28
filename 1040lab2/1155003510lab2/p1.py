# part1 q1
def romanNumber(arabic):
	if arabic>99:
		print "number is out of range"
		arabic = 99

	basic = ['I','II','III','IV','V','VI','VII','VIII','IX','XII']
	RomanDict = {}
	RomanDict['10'] = 'X'
	RomanDict['50'] = 'L'
	RomanDict['100'] = 'C'

	outStr = ''

	# -50 when it is >50; -90 when it is >90
	if arabic >= 90 and arabic <= 99:
		arabic -=90
		outStr += RomanDict['10'] + RomanDict['100']
	if arabic > 50 and arabic < 90:
		arabic -= 50
		outStr += RomanDict['50']
	if arabic == 50:
		outStr += RomanDict['50']

	digit = arabic%10
	ten = arabic/10

	# 0 - 9
	if ten==0:
		if digit != 0:
			outStr += basic[digit-1]
	# 10 - 39
	elif ten>=1 and ten <4:
		outStr += str(RomanDict['10']*ten)
		if digit != 0:
			outStr += str(basic[digit-1])
	# 40-49
	elif ten==4:
		outStr += str(RomanDict['10']) + str(RomanDict['50'])
		if digit != 0:
			outStr += str(basic[digit-1])

	# print outStr
	print "Roman equivalent:", outStr
#######
# prompt = "Please enter a arabic number: "
# number = input(prompt)
# romanNumber(number)
