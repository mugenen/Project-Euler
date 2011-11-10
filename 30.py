
import itertools
n = [i**5 for i in xrange(0, 10)]
s = 0
for i in itertools.product(xrange(10), repeat = 6):
	ss = sum([n[j] for j in i])
	st = ss
	flag = True
	for j in xrange(len(i)):
		if st % 10 != i[len(i) - j - 1]:
			flag = False
			break
		st /= 10
	if st > 0:
		flag = False
	if flag:
		print ss, i
		s += ss

print s - 1

443839
