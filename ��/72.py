
#http://d.hatena.ne.jp/Rion778/20090531/1243770304
#トーティエント
phi = range(2, 1000001)
for i in xrange(2, 1000001):
	if phi[i - 2] == i:
		for j in xrange(i - 2, len(phi), i):
			phi[j] = phi[j] * float(i - 1) / i

sum(phi)

