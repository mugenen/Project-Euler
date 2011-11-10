import itertools

MAX = 10**8 + 1
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


L = len(p)
MAX = 10**8
s = 0
for i in xrange(L):
	for j in xrange(i, L):
		if p[i] * p[j] >= MAX:
			break
		s += 1




