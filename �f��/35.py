import itertools

MAX = 1000000
prime = [-1] * MAX
i = 2
while MAX > i:
	if prime[i - 1] == -1:
		prime[i - 1] = 0
		temp = i * 2
		while temp < MAX:
			prime[temp - 1] = 1
			temp += i
	if i == 2:
		i += 1
	else:
		i += 2

s = 0
i = 2
#while MAX > i:
#	if prime[i - 1] == 0:
#		if i < 10:
#			s += 1
#			print i
#		else:
#			z = str(i)
#			if "2" in z or "4" in z or "6" in z or "8" in z:
#				pass
#			else:
#				f = True
#				for p in itertools.permutations(z):
#					p = int("".join(p))
#					if prime[p - 1] != 0:
#						f = False
#				if f:
#					s += 1
#					print i
#	if i == 2:
#		i += 1
#	else:
#		i += 2


while 10 > i:
	if prime[i - 1] == 0:
		s += 1
		print i
	if i == 2:
		i += 1
	else:
		i += 2

for j in range(2, 7):
	for i in itertools.product([1, 3, 7, 9], repeat = j):
		i = int("".join([str(w) for w in i]))
		if prime[i - 1] == 0:
			f = True
			for p in xrange(1, i):
				z = str(i)
				if prime[int(z[p:] +z[:p]) - 1] != 0:
					f = False
					break
			if f:
				s += 1
				print i

s
