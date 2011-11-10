
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

def Euler_totient(n):
	t = prime(n)
	ret = 1
	for p in t:
		ret *= (1 - 1.0 / p)
	return ret

s = 100
for i in xrange(1, 10 ** 6 + 1):
	m = Euler_totient(i)
	if s > m:
		s = m
		print i


#2*3*5*7*11*13ÇÁÇµÇ¢ÅcÅc
