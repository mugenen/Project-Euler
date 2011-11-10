

import itertools

s = 0
for i in itertools.count(1):
	f = True
	for j in xrange(9, 0, -1):
		if len(str(j**i)) == i:
			print i, j
			f = False
			s += 1
		else:
			break
	if f:
		break
		print s

