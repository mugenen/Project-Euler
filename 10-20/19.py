#def zeller(year, month, day):
#http://ja.wikipedia.org/wiki/%E3%83%84%E3%82%A7%E3%83%A9%E3%83%BC%E3%81%AE%E5%85%AC%E5%BC%8F
#	if month <= 2:
#		year -= 1
#		month += 12
#	J = year / 100
#	K = year % 100
#	return (day + (month + 1) * 26 / 10 + K + K / 4 + J / 4 + 5 * J) % 7

import datetime

s = 0
for i in xrange(0, 100):
	year = 1901 + i
	for j in xrange(1, 13):
#		if zeller(year, j, 1) == 1:
		if datetime.datetime(year, j, 1).weekday() == 6:
			s += 1

s
