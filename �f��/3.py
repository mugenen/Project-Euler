n = 600851475143
prime = []
i = 2
while i <= n:
	if n % i == 0:
		n = n / i
		if i not in prime:
			prime.append(i)
	else:
		if i != 2:
			i += 2
		else:
			i += 1

prime