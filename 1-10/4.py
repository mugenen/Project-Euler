ret = []
for i in xrange(100, 1000):
	for j in xrange(100, 1000):
		mul = str(i * j)
		if mul == mul[::-1]:
			ret.append(int(mul))

max(ret)
