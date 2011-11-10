

sq = []
for i in xrange(10):
	sq.append(i * i)

def cal(st):
	ss = 0
	for j in str(st):
		ss += sq[int(j)]
	return ss

ret = [-1] * 567
ret[0] = 0
ret[88] = 1
s = 0

for i in xrange(1, 10000001):
	r = cal(i)
#	print i, r, ret[r - 1]
	temp = []
	while ret[r - 1] == -1:
#		print i, r, ret[r - 1]
		temp.append(r)
		r = cal(r)
	for t in temp:
		ret[t - 1] = ret[r - 1]
	if ret[r - 1] == 1:
		s += 1

print s



#‰º‚Ì‚Ù‚¤‚ª‘‚¢H

sq = []
for i in xrange(10):
	sq.append(i * i)

def cal(st):
	ss = 0
	while st >= 10:
		ss += (st % 10) ** 2
		st /= 10
	ss += st ** 2
	return ss

ret = [-1] * 567
ret[0] = 0
ret[88] = 1
s = 0

for i in xrange(1, 568):
	r = cal(i)
	temp = []
	while ret[r - 1] == -1:
		temp.append(r)
		r = cal(r)
	for t in temp:
		ret[t - 1] = ret[r - 1]
	ret[i - 1] = ret[r - 1]

for i in xrange(1, 10000001):
	r = cal(i)
#	print i, r, ret[r - 1]
	if ret[r - 1] == 1:
		s += 1

print s


