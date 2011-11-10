import collections
import itertools

c = collections.Counter()

for i in xrange(1, 50000):
	l = list(str(i ** 3))
	l.sort()
	l = tuple(l)
	c[l] += 1
	if c[l] >= 5:
		print i, i ** 3
		break

t = []
for i in c.keys():
	if c[i] == 5:
		print i
		t = i

for i in xrange(1, 50000):
	l = list(str(i ** 3))
	l.sort()
	l = tuple(l)
	if l == t:
		print i ** 3
		break


