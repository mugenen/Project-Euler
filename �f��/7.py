prime = [2]
i = 3
c = 1
while 10000 >= c:
	fail = False
	for p in prime:
		if i % p == 0:
			i += 2
			fail = True
			break
	if not fail:
		prime.append(i)
		c += 1
		print i, c

max(prime)