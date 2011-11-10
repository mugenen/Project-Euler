import itertools

s = 0
qq = set()
for i in xrange(1, 3):
	for p in itertools.permutations(xrange(1, 10), 5):
		n = "".join([str(t) for t in p[:i]])
		m = "".join([str(t) for t in p[i:]])
		t = int(n) * int(m)
		z = [a for a in n + m + str(t)]
		if len(set(z)) == 9 and len(z) == 9 and "0" not in str(t):
#			print n, m, int(n) * int(m)
			s += t
			qq.add(t)

print sum(qq)


112740
