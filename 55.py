import math
def isPalindromic(n):
	t = str(n)
	return t == t[::-1]

s = 0

for i in xrange(1, 10000):
	f = False
	for j in xrange(49):
		e = int(str(i)[::-1])
		if isPalindromic(i + e):
			f = True
			break
		else:
			i = i + e
	if f:
		pass
	else:
		s += 1

s