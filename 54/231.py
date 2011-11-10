#http://d.hatena.ne.jp/rg350/20100708/1278566805
n = 20000000
r = 15000000

L = [0] * (n + 2)
S = [0] * (n + 2)
for i in xrange(2, n + 2):
	L[i] = i

for i in xrange(2, n + 2):
	for j in xrange(i, n + 2, i):
		if L[j] != 1:
			while L[j] % i == 0:
				L[j] /= i
				S[j] += i

s = 0
for i in xrange(r):
	s += S[n - i]
	s -= S[i + 1]

s

