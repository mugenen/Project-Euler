import itertools
import math

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

for n in [0, 1, 2, 3, 4]:
	for i in ["2", "3", "5", "7"]:
		for j in ["3","7"]:
			for k in itertools.product(["1", "3", "7", "9"], repeat = n):
				k = "".join(k)
				num = int(i + k + j)
				if prime[num - 1] == 0:
					flag = True
					for zz in xrange(len(k) + 1):
						qq = int(i + k[:zz])
						if prime[qq - 1] != 0:
							flag = False
							break
						qq2 = int(k[zz:] + j)
						if prime[qq2 - 1] != 0:
							flag = False
							break
					if flag:
						print num
						s += num

s
