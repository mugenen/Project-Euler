import math

s = 0
for i in xrange(8, 101):
	t = int(math.sqrt(i))
	for j in xrange(t, i / 4 + 2):
		z = j % 2
		if z == 0:
			z = 2
		for k in xrange(z, j - 1, 2):
			if -0.0001 <= j**2 - k **2 - i <= 0.0001:
				s += 1
				print (j - k) / 2, k, i
else:
	print s

##########################

import math

s = 0
MAX = 1000000
for i in xrange(1, int(math.sqrt(MAX)) / 2):
	for j in xrange(1, MAX / 4 - i + 1):
		t = 4 * i * (i + j)
		if t <= MAX:
			s += 1
else:
	print s

##########################

import math

s = 0
MAX = 1000000
for i in xrange(1, int(math.sqrt(MAX)) / 2):
	s += (MAX - 4 * i**2) / 4 / i
else:
	print s
