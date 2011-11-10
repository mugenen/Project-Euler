#コインの種類ごとにループ
for D in xrange(60000, 60001):
	MAX = D
	ret = [0] * (MAX + 1)
	ret[0] = 1
	
	for i in xrange(1, MAX):
		index = i
		
		while index <= MAX:
			ret[index] += ret[index - i]
			index += 1
	#	print ret

i = 0
for r in ret:
	if r % 1000000 == 0:
		print i
		break
	i += 1
