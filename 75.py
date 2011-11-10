import math
import fractions
import collections

def pythagorean(m, n):
	p = m**2
	q = n**2
	return (abs(p - q), 2*m*n, p + q)

c = collections.Counter()
m = 0
MAX = 1000
LIMIT = 1500000
for i in xrange(1, MAX):
	for j in xrange(i + 1, MAX, 2):
		if fractions.gcd(i, j) == 1:
			t = pythagorean(i, j)
			s = sum(t)
			z = s
			while z <= LIMIT:
				c[z] += 1
				z += s
				

A = 0
for k in c.keys():
	if c[k] == 1:
		A += 1
else:
	print A
