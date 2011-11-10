
	1	2	3	4	
1 	1	0
2	1	1
3	1	1	1
4	1	2	1	1
5	1	2	2	1	1
6	1	3

c(i, j) = c(i - 1, j - 1) + c(i - j, j)


memo = {}
def c(i, j):
	if j <= 1 or i == j:
		return 1
	if i < j:
		return 0
	if(memo[(i, j)] != 0):
		return memo[(i, j)]
	memo[(i, j)] = c(i - 1, j - 1) + c(i - j, j)
	return memo[(i, j)]

def d(n):
	s = 0
	for i in xrange(n):
		s += c(n, i + 1)
	return s

import itertools

for i in itertools.count(1):
	t = d(i)
	print i, t
	if t % 1000000 == 0:
		break
