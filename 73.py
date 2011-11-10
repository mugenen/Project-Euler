
import fractions
m = 1/ 3.0
s = 0
for i in xrange(1, 12001):
	for j in xrange(int(m * i) + 1, i / 2 + 1):
		if j / float(i) >= 1 / 2.0:
			break
		if j / float(i) <= 1 / 3.0 or fractions.gcd(i, j) != 1:
			continue
		s += 1

s
