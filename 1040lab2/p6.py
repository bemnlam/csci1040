class TextProcessor(object):
	vowel = ['A','E','I','O','U']
	@staticmethod
	def stringReversal(string):
		return string[::-1]
	@staticmethod
	def vowelCapitalization(string):
		tmpStr = string
		for v in TextProcessor.vowel:
			tmpStr = tmpStr.replace(v.lower(), str(v))
		return tmpStr
