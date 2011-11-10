reduce(lambda x, y: x * y, xrange(1,11)) > 1000000
X
reduce(lambda x, y: x * y, xrange(1,10)) * 3 > 1000000
reduce(lambda x, y: x * y, xrange(1,9)) * 7 > 274240

27

01345689

274240



import math

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 1000000.0
i = 10
temp = reduce(lambda x, y: x * y, xrange(1, i))

while len(n) > 1:
	div = reduce(lambda x, y: x * y, xrange(1, i))
	z = math.ceil(num / div)
	print z, num, div, n
	n.pop(int(z) - 1)
	num -= div * (z - 1)
	i -= 1


ans = 2783915460



import itertools
i = 1
for it in itertools.permutations(xrange(10), 10):
	if i == 1000000:
		print "".join([str(q) for q in it])
		break
	i += 1
