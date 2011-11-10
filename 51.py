#ŽQl
#http://tsumuji.cocolog-nifty.com/tsumuji/2009/08/project-euler-7.html
#http://pamgau.net/item/721
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
	
	z = str(p[i])
	index = []
	for j in xrange(3):
		for u in xrange(len(z)):
			if z[u] == str(j):#0, 1, 2‚Ì‚¢‚¸‚ê‚©
				index.append(u)
		zzzz = []
		
		if len(index) >= 3:
			print p[i], index
			for tindex in itertools.combinations(index, 3):
				qu = 0
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
	if success:
		break

