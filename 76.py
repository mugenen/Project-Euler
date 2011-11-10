
#コインの種類ごとにループ
MAX = 100
ret = [0] * (MAX + 1)
ret[0] = 1

for i in xrange(1, MAX):
	index = i
	
	while index <= MAX:
		ret[index] += ret[index - i]
		index += 1
#	print ret

print ret[MAX]


#DP版
MAX = 100
ret = [[0] * MAX for i in xrange(MAX)]
ret[0][0] = 1
for i in xrange(MAX):
	ret[i][0] = 1

for i in xrange(1, MAX):
	for j in xrange(1, i + 1):
		print i, j
		if i - j - 1 >= j:
			ret[i][j] = ret[i - 1][j - 1] + ret[i - j - 1][j]
#			print (i, j), (i-1, j-1), (i - j, j)
		else:
			ret[i][j] = ret[i - 1][j - 1]

print sum(ret[MAX - 1]) - 1
