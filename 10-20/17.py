s = 0
d = {}
d[0] = 4
d[1] = 3
d[2] = 3
d[3] = 5
d[4] = 4
d[5] = 4
d[6] = 3
d[7] = 5
d[8] = 5
d[9] = 4

e = {}
e[0] = 6
e[1] = 6
e[2] = 5
e[3] = 5
e[4] = 5
e[5] = 7
e[6] = 6
e[7] = 6

g = {}
g[0] = 3
g[1] = 6
g[2] = 6
g[3] = 8
g[4] = 8
g[5] = 7
g[6] = 7
g[7] = 9
g[8] = 8
g[9] = 8
for i in xrange(1, 1001):
	if i == 1000:
		s += 11
		continue
	c = 0
	while i >= 100:
		i -= 100
		c += 1
	if c > 0:
		s += 10
		s += d[c]
		if i == 0:
			s -= 3
			continue
	f = 0
	while i >= 20:
		i -= 10
		f += 1
	if f > 0:
		s += e[f - 1]
		i -= 10
		if i == 0:
			continue
	if i >= 10:
		s += g[i - 10]
	else:
		s += d[i]

s