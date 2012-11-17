#http://d.hatena.ne.jp/rahaema/20121116/p1
import itertools
import math

MAX = 1000000
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

count = 0
s = 0
for div in p:
    if pow(10, 10 ** 9, 9 * div) == 1:
        count += 1
        s += div
        
        if count >= 40:
            print 'Exit!'
            break

print s