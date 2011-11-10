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

k = 2
prime = {}
prime['3'] = set(['3'])
while True:
	i = 6 * k - 5
	if is_prime3(i):
		st = str(i)
		done = False
		prime[st] = set([st])
		for j in prime.keys():
			if is_prime3(int(st + j)) and is_prime3(int(j + st)):
				prime[st].add(j)
				prime[j].add(st)
				th = 5
				if len(prime[st]) >= th:
					prob = []
					for y in prime[st]:
						z = set(prime[st])
						if len(z & prime[y]) >= th:
							prob.append(y)
					if len(prob) < th:
						continue
					for e in itertools.combinations(prob, th):
						z = set(prime[st])
						for w in e:
							z &= prime[w]
							if len(z) < th:
								break
						if len(z) >= th:
							done = True
							print z, "done"
							break
					if done:
						break
		if done:
			break
	
	i = 6 * k - 1
	if is_prime3(i):
		st = str(i)
		done = False
		prime[st] = set([st])
		for j in prime.keys():
			if is_prime3(int(st + j)) and is_prime3(int(j + st)):
				prime[st].add(j)
				prime[j].add(st)
				th = 5
				if len(prime[st]) >= th:
					prob = []
					for y in prime[st]:
						z = set(prime[st])
						if len(z & prime[y]) >= th:
							prob.append(y)
					if len(prob) < th:
						continue
					for e in itertools.combinations(prob, th):
						z = set(prime[st])
						for w in e:
							z &= prime[w]
							if len(z) < th:
								break
						if len(z) >= th:
							done = True
							print z, "done"
							break
					if done:
						break
		if done:
			break
	print i
	k += 1
