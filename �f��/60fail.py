

import itertools
import math
import random

#http://d.hatena.ne.jp/pashango_p/20090704/1246692091
def is_prime3(q,k=50):
	q = abs(q)
	if q == 2: return True
	if q < 2 or q&1 == 0: return False
	
	d = (q-1)>>1
	while d&1 == 0:
		d >>= 1
	
	for i in xrange(k):
		a = random.randint(1,q-1)
		t = d
		y = pow(a,t,q)
		while t != q-1 and y != 1 and y != q-1: 
			y = pow(y,2,q)
			t <<= 1
		if y != q-1 and t&1 == 0:
			return False
	return True

k = 3
prime = {}
prime['3'] = set(['3'])
prime['7'] = set(['7'])
prime['11'] = set(['11'])
while True:
	i = 6 * k - 5
	if is_prime3(i):
		st = str(i)
		prime[st] = set([st])
		done = False
		for j in xrange(1, len(st)):
			head = st[:j]
			tail = st[j:]
			rev = int(tail + head)
			if str(rev) not in prime and is_prime3(rev) and head in prime and tail in prime:
				prime[head].add(tail)
				prime[tail].add(head)
#				print st, rev, prime[head], prime[tail], head, tail
				th = 5
				if len(prime[head]) >= th:
					z = set(prime[head])
					for w in prime[head]:
						z &= prime[w]
					if len(z) >= th:
						done = True
						print z, "done"
						break
				if len(prime[tail]) >= th:
					z = set(prime[tail])
					for w in prime[tail]:
						z &= prime[w]
					if len(z) >= th:
						done = True
						print z, "done"
						break
		if done:
			break
	
	print i
	i = 6 * k - 1
	if is_prime3(i):
		st = str(i)
		prime[st] = set([st])
		done = False
		for j in xrange(1, len(st)):
			head = st[:j]
			tail = st[j:]
			rev = int(tail + head)
			if str(rev) not in prime and is_prime3(rev) and head in prime and tail in prime:
				prime[head].add(tail)
				prime[tail].add(head)
#				print st, rev, prime[head], prime[tail], head, tail
				th = 5
				if len(prime[head]) >= th:
					z = set(prime[head])
					for w in prime[head]:
						z &= prime[w]
					if len(z) >= th:
						done = True
						print z, "done"
						break
				if len(prime[tail]) >= th:
					z = set(prime[tail])
					for w in prime[tail]:
						z &= prime[w]
					if len(z) >= th:
						done = True
						print z, "done"
						break
		if done:
			break
	print i
	k += 1


13 5197 5701 6733 8389
26033
