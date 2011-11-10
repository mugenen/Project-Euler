def tri(n):
	return (1 + n) * n / 2

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

j = 8
while True:
	temp = tri(j)
	p = prime(temp)
	mul = 1
	for q in p:
		mul *= (p[q] + 1)
	print j, mul, temp
	if mul - 1 >= 500:
		break
	j += 1
