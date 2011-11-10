import itertools
import math

s = 0

for i in xrange(0, 5):
	n = 2 * i + 1
	q = format(n, "b")
	print n, q
	s += n

for i in xrange(1, 1000):
	n = i
	t = str(n)
	z = int(t + t[::-1])
	
	q = format(z, "b")
	qd = int(math.floor(len(q) / 2.0))
	qu = int(math.ceil(len(q) / 2.0))
	
	if q[:qd] == q[qu:][::-1]:
		print z, q
		s += z
	if i < 100:
		for j in xrange(0, 10):
			z2 = int(t + str(j) + t[::-1])
			q = format(z2, "b")
			qd = int(math.floor(len(q) / 2.0))
			qu = int(math.ceil(len(q) / 2.0))
			if q[:qd] == q[qu:][::-1]:
				print z2, q
				s += z2

s
