import itertools

memo = {}

def d(n):
	if n == 0:
		return 1
	if n < 0:
		return 0
	if n in memo:
		return memo[n]
	s = 0
	for i in itertools.count(1):
		t = n - (3*i*i - i) / 2.0
		t2 = n - (3*i*i + i) / 2.0
		s += (-1) ** (i + 1) * d(t)
		s += (-1) ** (i + 1) * d(t2)
		if t2 < 0:
			break
	memo[n] = s
	return s

for i in itertools.count(1):
	t = d(i)
	if t % 1000000 == 0:
		print i, t
		break
