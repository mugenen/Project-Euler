
def isPentagonal(q):
	x = (1 + math.sqrt(1 + 24 * q)) / 6.0
	return int(x) == x

def isTriagonal(q):
	x = (1 + math.sqrt(1 + 8 * q)) / 2.0
	return int(x) == x

import itertools
for i in itertools.count(144):
	n = i * (2 * i - 1)
	if isPentagonal(n) and isTriagonal(n):
		print n
		break

