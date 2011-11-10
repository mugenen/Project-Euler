MAX = 2000000
prime = [-1] * MAX
i = 2
while MAX > i:
	if prime[i - 1] == -1:
		prime[i - 1] = 0
		temp = i * 2
		while temp < MAX:
			prime[temp - 1] = 1
			temp += i
	if i == 2:
		i += 1
	else:
		i += 2

m = 0
for p in xrange(-1000, 1001):
	for q in xrange(-1000, 1001):
		if prime[q - 1] != 0:
			continue
		c = 0
		i = 0
		while i < b:
			n = i * i + p * i + q
			if n < 1:
				break
			i += 1
			if prime[n - 1] == 0:
				c += 1
			else:
				break
		if c > m:
			m = c
			print c, p, q


ans = -61 * 971 = -59231
