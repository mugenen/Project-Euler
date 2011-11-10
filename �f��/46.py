import itertools
import math

MAX = 10000
prime = [-1] * MAX
i = 2
p = []
while MAX > i:
	if prime[i - 1] == -1:
		prime[i - 1] = 0
		p.append(i)
		temp = i * 2
		while temp < MAX:
			prime[temp - 1] = 1
			temp += i
	if i == 2:
		i += 1
	else:
		i += 2

import itertools
import math

for i in itertools.count(2):
	odd = 2 * i + 1
	if prime[odd - 1] == 0:
		continue
	f = True
	for pp in p:
#		print odd, pp
		if pp > odd:
			break
		if (odd - pp) % 2 == 0 and math.sqrt((odd - pp) / 2.0) == int(math.sqrt((odd - pp) / 2.0)):
			f = False
			break
	if f:
		print odd
		break
