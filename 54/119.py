#http://blog.dreamshire.com/2009/04/20/project-euler-problem-119-solution/
import itertools
import math
a = []
n = 30
for b in xrange(2, 600):
	for e in xrange(2, 50):
 		p = b ** e
		if sum(map(int, str(p))) == b:
			a.append(p)
		if len(a) > n * 1.1:
			break

a.sort()