import itertools

s = 0
for i in itertools.permutations([str(n) for n in xrange(0, 10)]):
	x = "".join(i)
	n = int(x)
	if int(x[1:4]) % 2 == 0 and int(x[2:5]) % 3 == 0 and int(x[3:6]) % 5 == 0 and int(x[4:7]) % 7 == 0 and int(x[5:8]) % 11 == 0 and int(x[6:9]) % 13 == 0 and int(x[7:10]) % 17 == 0:
		print n
		s += n

s