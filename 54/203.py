#http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
def comb(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


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

import itertools
s = set()
for i in xrange(1, 51):
	for j in xrange(1, int(math.ceil(i / 2.0)) + 1):
		s.add(comb(i, j))

ss = 0
for q in s:
	f = True
	for pp in p:
		if pp**2 > q:
			break
		if q % (pp**2) == 0:
			f = False
			break
	
	if f:
		ss += q

ss
