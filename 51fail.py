import itertools
import math

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

L = len(p)

s = 0

success = False
for i in xrange(5683, L - 8):
	for j in xrange(i + 1, L - 7):
		diff = p[j] - p[i]
		qu = 0
		if p[j] + diff > MAX:
			break
#		print  p[i], p[j], diff
		z = str(p[i])
		zz = str(p[j])
		if len(z) < len(zz):
			break
		elif len(z) > len(zz):
			continue
		index = []
		for u in xrange(len(z)):
			if z[u] == 0:#0, 1, 2‚Ì‚¢‚¸‚ê‚©
				index.append(u)
		zzzz = []
		
		if len(index) >= 3:
			print p[i], p[j], index
			tt = list(z)
			for w in xrange(10):
				rrr = False
				for ii in index:
					if w == 0 and ii == 0:
						rrr = True
						break
					tt[ii] = str(w)
				if rrr:
					continue
				if prime[int("".join(tt)) - 1] == 0:
					qu += 1
					zzzz.append(int("".join(tt)))
		if qu >= 8:
			for r in zzzz:
				print r,
			print 
			success = True
			break
	if success:
		break
