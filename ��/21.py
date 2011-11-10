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

result = [0] * 10000
s = 0
for i in range(2, 10000):
	p = prime(i)
	mul = 1
	for q in p:
		n = p[q]
		ret = sum(map(lambda x:q ** x, xrange(0, n + 1)))
		mul *= ret
	mul -= i
	if  mul > i:
		result[i] =  mul
	elif result[mul] == i:
		s += i
		s += mul

s