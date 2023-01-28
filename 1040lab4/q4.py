import re
import urllib

def getStockPrice(url):
	remotefile = urllib.urlopen(url)
	line = remotefile.readline()
	magic_str = 'class="time_rtq_ticker">'
	while line:
		if magic_str in line:
			#lst = line.split()
			#for str in lst:
				if magic_str in line:
					re_lst = re.findall(r'\d+', line)
					price = (int(re_lst[3]) + int(re_lst[4])/1000.0)
					return '%.3f' % price
		line = remotefile.readline()
	return "err"

fpath = 'Lab4/StockCode.txt'
stock_dict = {}
f = open(fpath, 'r')

for line in f.readlines():
	lst = line.split('\t')
	stock_dict[lst[0]] = lst[1]

while True:
	user_code = raw_input("Please enter a stock quote: ")
	if user_code == '9999':
		exit(0)

	if user_code in stock_dict:
		url = "http://hk.finance.yahoo.com/q?s=%04d.HK" % int(user_code)
		print 'The price of '+ stock_dict[user_code] + " is " + getStockPrice(url)
	else:
		print "> no such stock code: " + user_code
