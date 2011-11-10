import itertools
import math

for i in itertools.count(2):
	a = list(str(i))
	a.sort()
	c = 0
	for j in xrange(2, 7):
		b = list(str(i * j))
		b.sort()
		if a == b:
			c += 1
	if c >= 5:
		print i

