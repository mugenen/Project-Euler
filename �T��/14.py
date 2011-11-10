l = [0] * 1000000
l[0] = 1

def sl(n):
	if n < 1000000:
		if l[n - 1] != 0:
			return l[n - 1]
		else:
			if n % 2 == 0:
				l[n - 1] = sl(n / 2) + 1
				return l[n - 1]
			else:
				l[n - 1] = sl(3 * n + 1) + 1
				return l[n - 1]
	else:
		if n % 2 == 0:
			return sl(n / 2) + 1
		else:
			return sl(3 * n + 1) + 1

m = 0
num = -1
for i in xrange(1, 1000000):
	t = sl(i)
	if t > m:
		m = t
		num = i

num












l = [0] * 1000000
l[0] = 1
m = 0
num = -1
for i in xrange(2, 1000000):
	h = i
	c = 0
	while h >= i:
		c += 1
		if h % 2 == 0:
			h = h / 2
		else:
			h = 3 * h + 1
	dist = c + l[h]
	l[i] = dist
	if dist > m:
		m = dist
		num = i

num