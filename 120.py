#n is even:
#	2
#n is odd:
#	2 * n * a % a**2

s = 0
for a in xrange(3, 1001):
	n = 1
	r = []
	while True:
		div = a**2
		rem = 2 * n * a % div
		if rem in r:
			s += max(r)
			break
		else:
			r.append(rem)
			n += 2
else:
	print s

