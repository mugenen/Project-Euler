import math

n = 1
d = 2

s = 0
for i in xrange(3, 1001):
	print n + d, d
	n = 2 * d + n
	n, d = d, n
	if len(str(n + d)) > len(str(d)):
		s += 1

s
