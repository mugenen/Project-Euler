import fractions

def num(n):
	if n % 3 == 0:
		return 2 * n / 3
	else:
		return 1


N = 100
t = fractions.Fraction(1, num(N))
for i in xrange(N, 2, -1):
	t = num(i - 1) + t
	t = 1 / t

print 2 + t
q = 2 + t

sum([int(i) for i in str(q.numerator)])