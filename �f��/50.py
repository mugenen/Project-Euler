import itertools
import math

MAX = 1000000
prime = [-1] * MAX
i = 2
p = []
while MAX > i:
	if prime[i - 1] == -1:
		prime[i - 1] = 0
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

for i in xrange(L):
	s += p[i]
	print i, s
	if s > MAX:
		s = i
		break

LIMIT = s - 1

s = 0

for i in xrange(LIMIT, 0, -1):
	success = False
	for j in xrange(L - LIMIT):
		ss = 0
		fail = False
		for k in xrange(j, j + i):
			ss += p[k]
			if ss > MAX:
				fail = True
				break
#		print i, p[j], ss
		if not fail and prime[ss - 1] == 0:
			print ss
			success = True
			break
	if success:
		break
