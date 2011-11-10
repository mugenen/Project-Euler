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

def sum_of_divisors(i):
	p = prime(i)
	mul = 1
	for q in p:
		n = p[q]
		ret = sum(map(lambda x:q ** x, xrange(0, n + 1)))
		mul *= ret
	return mul - i

abundant = set()
MAX = 28123
for i in range(12, MAX):
#abundant number
	mul = sum_of_divisors(i)
	if mul > i:
		t = i
		while t < MAX:
			abundant.add(t)
			t += i

s = 0
for i in range(1, MAX):
	if i < 24:
		s += i
		continue
	f = True
	for j in abundant:
		z = i - j
		if z > 0 and z in abundant:
			f = False
			break
	if f:
		s += i

s
