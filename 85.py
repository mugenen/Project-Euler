#1x1 wxh


#2x1 (w - 1)*h

import itertools
index = 0
for i in itertools.count(1):
	w = h = i
	s = 0
	for x in xrange(1, w + 1):
		for y in xrange(1, h + 1):
			s += (w - x + 1) * (h - y + 1)
	else:
		print i, s
		if s >= 2000000:
			index = i
			break

diff = 2000000
for i in xrange(-30, 31):
	for j in xrange(-30, 31):
		s = 0
		w = index + i
		h = index + j
		for x in xrange(1, w + 1):
			for y in xrange(1, h + 1):
				s += (w - x + 1) * (h - y + 1)
		else:
			if abs(2000000 - s) < diff:
				diff = abs(2000000 - s)
				print w, h, w * h, diff

