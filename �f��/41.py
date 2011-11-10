import itertools
import math

def isPrime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in xrange(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True


chk = []
for j in xrange(1, 10):
	chk.append(set([str(w) for w in xrange(1, j + 1)]))

i = 3
for j in xrange(1, 10):
	for i in itertools.permutations(xrange(1, 9), j):
		i = int("".join([str(n) for n in i]))
		if isPrime(i):
	#		print i, set(str(i)), chk[len(str(i)) - 1], set(str(i)) & chk[len(str(i)) - 1]
			if len(set(str(i)) & chk[len(str(i)) - 1]) == len(str(i)):
				print i

