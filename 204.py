##########Fail
from itertools import * 

MAX = 6
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

s = 0
T = 10 ** 8
for i in xrange(1, 4):
	for j in combinations(p, i):
		m = 1
		for n in j:
			m *= n
		if i % 2 == 1:
			s += T / m
		else:
			s -= T / m

##########Memory Error

from itertools import * 

MAX = 101
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


MAX = 10**9
ham = [-1] * MAX
ham[0] = 1
s = 1
for q in p:
#	ham[q - 1] = 1
#	s += 1
	for i in xrange(1, MAX):
		if ham[i - 1] == 1:
			temp = i * q
			while temp < MAX:
				if ham[temp - 1] == -1:
					s += 1
				ham[temp - 1] = 1
				temp *= q
else:
	print s

###############


from itertools import * 

MAX = 101
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

r = range(len(p))
f = lambda i,a: 1 + sum(f(j, a*p[j]) for j in r[i:] if a*p[j] <= 10**9)
print 1 + sum(f(i, p[i]) for i in r)

#http://d.hatena.ne.jp/yatt/20091227/1261935024
#p 2 3 5
#1 + 
#	2:1 + 
#		4:1 +
#		6:
#		10:
#	3:1 +
#		9:
#		15:
#	5:1 +
