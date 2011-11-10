import random
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

#コインの種類ごとにループ
for D in xrange(50, 100):
	MAX = D
	ret = [0] * (MAX + 1)
	ret[0] = 1
	
	for i in xrange(2, MAX):
		index = i
		if not is_prime3(i):
			continue
		
		while index <= MAX:
			ret[index] += ret[index - i]
			index += 1
	#	print ret
	
	print ret[MAX]
#	print ret
	if ret[MAX] > 5000:
		print D
		break
