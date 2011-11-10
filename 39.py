
m = 0
za = 0
for p in xrange(3, 1000):
	n = 0
	for a in xrange(1, p / 3):
		for b in xrange(a, (1000 - a) / 2 + 1):
			c = p - a - b
			if c < b:
				continue
			if a**2 + b**2 == c**2:
				print p, a, b, c
				n += 1
	if n > m:
		m = n
		za = p

za