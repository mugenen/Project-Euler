import itertools
import math

#http://www.geocities.jp/m_hiroi/light/python03.html
f = [math.factorial(i) for i in xrange(10)]

for i in xrange(3, 2540161):
	t = [int(x) for x in str(i)]
	s = 0
	for q in t:
		s += f[q]
	if s == i:
		print s
		

40730
