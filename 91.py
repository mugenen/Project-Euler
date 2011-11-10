s = 0
M = 51
for i in xrange(M):
	for j in xrange(M):
		if i == 0 and j == 0:
			continue
		for k in xrange(i, M):
			for l in xrange(M):
				if (k == i and l == j) or (k == 0 and l == 0) or (i * l - j * k == 0):
					continue
#				print i, j, k, l, (i*(k - i) + j* (l - j)) * (-k*(k - i) + -l* (l - j))* (i*(-l) + j* (-k))
				if (i*(k - i) + j* (l - j)) * (-k*(k - i) + -l* (l - j))* (i*(-l) + j* (-k)) == 0:
#				ƒsƒ^ƒSƒ‰ƒX‚Ì’è—‚Å‚¢‚¢‚æ‚Ë‚— 
					s += 1
else:
	print s