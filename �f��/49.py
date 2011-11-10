import itertools
import math

MAX = 10000
prime = [-1] * MAX
i = 2
p = []
while MAX > i:
	if prime[i - 1] == -1:
		prime[i - 1] = 0
		if i >= 1000:
			p.append(i)
		temp = i * 2
		while temp < MAX:
			prime[temp - 1] = 1
			temp += i
	if i == 2:
		i += 1
	else:
		i += 2

s = 0

L = len(p)
for i in xrange(L - 2):
	n = p[i]
	s = list(str(n))
	s.sort()
	for j in xrange(i + 1, L - 1):
		m = p[j]
		t = list(str(m))
		t.sort()
		if s != t:
			continue
		for k in xrange(j + 1, L):
			l = p[k]
			u = list(str(l))
			u.sort()
			if t == u and l - m == m - n:
				f = True
				print n, m, l

