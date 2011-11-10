inport random


r = 0
for j in xrange(100000000):
	s = 0
	for i in xrange(6):
		s += random.randint(1, 6)
	
	s2 = 0
	for i in xrange(9):
		s2 += random.randint(1, 4)
	
	if s2 > s:
		r += 1

r

#下側がまとも

import math

def min_dice(f):
	return f

def max_dice(f, p):
	return f * p

def comb(n, r):
	if n == 0 or r == 0: return 1
	return comb(n, r - 1) * (n - r + 1) / r

def freq_dice(f, p, s):
	t = 0
	for i in xrange(0, int(math.floor((s - f) / float(p))) + 1):
		t += comb(s - p * i - 1, f - 1) * comb(f, i) * (-1) ** i
	
	return t

def prob_dice(f, p, s):
	return freq_dice(f, p, s) / float(p ** f)


s = 0
for i in xrange(min_dice(4), max_dice(9, 4) + 1):
	for j in xrange(min_dice(6), max_dice(6, 6) + 1):
		if i > j:
			s += prob_dice(9, 4, i) * prob_dice(6, 6, j)

math.round(s)


#ダイスはクラス化すべき
