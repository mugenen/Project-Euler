#http://d.hatena.ne.jp/rg350/20100716/1279267771
MAX = 10000000

div = [0] * MAX

for i in xrange(1, MAX):
	for j in xrange(i, MAX, i):
		div[j] += 1


s = 0
for i in xrange(2, 10**7 - 1):
	if div[i] == div[i + 1]:
		s += 1

s
