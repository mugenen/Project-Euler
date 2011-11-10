
import math

def d_fac(n):
	s = 0
	for i in list(str(n)):
		s += math.factorial(int(i))
	return s


memo = {}

s = 0
for i in xrange(1, 1000000):
	t = []
	ss = 0
	n = i
	for j in xrange(60):
		if n in memo:
			ss += memo[n]
			break
		if n in t:
			break
		t.append(n)
		ss += 1
		n = d_fac(n)
	
	memo[i] = ss
	if ss >= 60:
		s += 1

#402