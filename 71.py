
import fractions
m = 0
for i in xrange(1, 1000001):
	for j in xrange(int(m * i) + 1, i / 2):
		if j / float(i) >= 3 / 7.0 or fractions.gcd(i, j) != 1:
			break
		if j / float(i) <= m:
			continue
		m = j / float(i)
		print j, i
