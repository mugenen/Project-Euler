
phi = range(2, 10 ** 7 + 1)
for i in xrange(2, 10 ** 7 + 1):
	if phi[i - 2] == i:
		for j in xrange(i - 2, len(phi), i):
			phi[j] = phi[j] * float(i - 1) / i


m = 10000
for i in xrange(5000000, 10000001):
	l = list(str(i))
	l.sort()
	l2 = list(str(int(phi[i - 2])))
	l2.sort()
	if l == l2:
		if m > i/ phi[i - 2]:
			m = i/ phi[i - 2]
			print i, l, l2, m

