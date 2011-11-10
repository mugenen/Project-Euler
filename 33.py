import itertools

#http://www.geocities.jp/m_hiroi/light/python03.html
def gcd(a, b):
	if b == 0: return a
	return gcd(b, a % b)

s1 = 1
s2 = 1
for i in xrange(10, 100):
	t = str(i)
	for j in xrange(i + 1, 100):
		if i % 10 == 0 or i % 11 == 0 or gcd(i, j) == 1:
			continue
		prob = []
		t2 = str(j)
		for l in xrange(2):
			for m in xrange(2):
				if t[l] == t2[m] and int(t2[1 - m]) / gcd(int(t[1 - l]), int(t2[1 - m])) == int(j) / gcd(i, j) and int(t[1 - l]) / gcd(int(t[1 - l]), int(t2[1 - m])) == int(i) / gcd(i, j):
					print t, t2,j / gcd(i, j)
					s1 *= i
					s2 *= j

print s2 / gcd(s1, s2)

