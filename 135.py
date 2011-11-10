#http://d.hatena.ne.jp/Rion778/20110508/1304854661
import collections
MAX = 10**6
c = collections.Counter()
for x in xrange(1, MAX):
	j = 4 - x % 4
	while j < 3 * x and x * j < MAX:
		c[x * j] += 1
		j += 4
else:
	s = 0
	for k in c.keys():
		if c[k] == 10:
			s += 1
	else:
		print s