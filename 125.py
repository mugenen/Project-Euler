import math
MAX = 10**8
t = int(math.sqrt(MAX))
p = []
for i in xrange(1, t):
	p.append(i**2)

s = 0
a = {}
for j in xrange(t - 2):
	s = p[j]
	k = 1
	while s <= MAX:
		s += p[j + k]
		k += 1
		z = str(s)
		if z == z[::-1] and s <= MAX:
#			print s, p[j:j+k]
			a[s] = True


ss = 0
for q in a.keys():
	ss += q
else:
	print ss
