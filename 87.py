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

s = set()


p2 =[]
p3 =[]
p4 =[]
for i in p:
	p2.append(i**2)
	p3.append(i**3)
	p4.append(i**4)


for i in p2:
	for j in p3:
		for k in p4:
			zz = i + j + k
			if i + j + k >= 50000000:
				break
			
			s.add(zz)

len(s)