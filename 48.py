
import math

#http://www.geocities.jp/m_hiroi/light/pyalgo01.html
def comb(n, r):
    if n == 0 or r == 0: return 1
    return comb(n, r - 1) * (n - r + 1) / r 

def pownlt(x, n, c):
	a = 10 ** x
#	print (a - n) ** (a - n)
	ss = 0
	for i in xrange(a - n + 1):
		if i * x > c:
			t = 10 ** (c + 1)
		else:
			t = comb(a - n, i) * a ** i * n ** (a - n - i)
		
		if (a - n + 1) % 2 == 0:
			if i % 2 == 0:
				ss -= t
			else:
				ss += t
		else:
			if i % 2 == 0:
				ss += t
			else:
				ss -= t
#		print i, a ** i, n ** (a - n - i), (a - n - i), ss, t
#	print ss % 10 ** c
	return ss % 10 ** c


#pownlt(1, 7, 1)
#pownlt(1, 8, 1)

s = 0
for i in xrange(1, 1000):
	s += pownlt(3, i, 10)

s % 10 ** 10
