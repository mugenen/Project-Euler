for c in xrange(997, 2, -1):
	for b in xrange(c - 1, 0, -1):
		a = 1000 - b - c
		if a**2 + b**2 == c**2:
			print a*b*c
