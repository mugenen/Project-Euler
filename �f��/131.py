#http://d.hatena.ne.jp/jeneshicc/20081206/1228548718
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
for i in itertools.count(1):
    p_cand = 3 * i * (i + 1) + 1
    if p_cand >= 1000000:
        break
    if prime[p_cand - 1] == 0:
        count += 1

print count
