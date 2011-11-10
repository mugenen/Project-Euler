prime = [-1] * 2000000
i = 2
while 2000000 > i:
	if prime[i - 1] == -1:
		prime[i - 1] = 0
		temp = i * 2
		while temp < 2000000:
			prime[temp - 1] = 1
			temp += i
	if i == 2:
		i += 1
	else:
		i += 2

sum = 0
i = 2
while 2000000 > i:
	if prime[i - 1] == 0:
		sum += i
	if i == 2:
		i += 1
	else:
		i += 2

sum
