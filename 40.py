d = 0
nn = [1, 10, 100, 1000, 10000, 100000, 1000000]
s = 1
for i in xrange(1, 1000000):
	t = len(str(i))
	for j in nn:
		if d + t >= j and d < j:
			print str(i), str(i)[j - d - 1]
			s *= int(str(i)[j - d - 1])
	d += t
	if d > 1000000:
		break

s
