import math
def isPalindromic(n):
	t = str(n)
	return t == t[::-1]

m = 0

for i in xrange(1, 101):
	for j in xrange(1, 101):
		m = max(m, sum([int(z) for z in str(i ** j)]))

m
