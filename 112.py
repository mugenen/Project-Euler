
import itertools

def isBouncy(n):
	t = list(str(n))
	t.sort()
	num = list(str(n))
	if num == t or num == t[::-1]:
		return 0
	else:
		return 1

s = 0
for i in itertools.count(1):
	s += isBouncy(i)
	if s / float(i) >= 0.99:
		print i, s
		break
