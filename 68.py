#http://d.hatena.ne.jp/Rion778/20090527/1243406949
import itertools
ret = []
for p in itertools.permutations(xrange(1, 6)):
	t = []
	for i in xrange(4):
		t.append(sum(p[i:i+2]))
	t.append(p[0] + p[-1])
	t.sort()
	if t == [4, 5, 6, 7, 8]:
		print p
		ret.append(p)

max(ret)

#6, 5, 3
#10, 3, 1
#9, 1, 4
#8, 4, 2
#7, 2, 5
#6531031914842725
