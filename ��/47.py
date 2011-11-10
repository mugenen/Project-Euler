def prime(n):
	p = {}
	def add(i):
		if i in p:
			p[i] += 1
		else:
			p[i] = 1
	i = 2
	while i <= n:
		if n % i == 0:
			n = n / i
			add(i)
		else:
			if i != 2:
				i += 2
			else:
				i += 1
	return p

i = 644
c = 0
while True:
	c = 0
	for j in xrange(3, -1, -1):
		if len(prime(i + j)) == 4:
			c += 1
		else:
			i += j + 1
			break
	if c >= 4:
		print i, prime(i + 0), prime(i + 1), prime(i + 2), prime(i + 3)
		break

i
