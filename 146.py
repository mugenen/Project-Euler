import random
def is_prime3(q,k=5):
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


s = 0
for i in xrange(10, 150000000, 10):
	n = i**2
	if is_prime3(n + 1) and is_prime3(n + 3) and is_prime3(n + 7) and is_prime3(n + 9) and is_prime3(n + 13) and is_prime3(n + 27):
		if not(is_prime3(n + 5) or is_prime3(n + 11) or is_prime3(n + 15) or is_prime3(n + 17) or is_prime3(n + 19) or is_prime3(n + 21) or is_prime3(n + 23) or is_prime3(n + 25)):
			print i
			s += i
else:
	print s




#####################
s = 0
for i in xrange(10, 150000000, 10):
	n = i**2
	if n % 30 != 10:
		continue
	if is_prime3(n + 1) and is_prime3(n + 3) and is_prime3(n + 7) and is_prime3(n + 9) and is_prime3(n + 13) and is_prime3(n + 27):
		if not(is_prime3(n + 5) or is_prime3(n + 11) or is_prime3(n + 15) or is_prime3(n + 17) or is_prime3(n + 19) or is_prime3(n + 21) or is_prime3(n + 23) or is_prime3(n + 25)):
			print i
			s += i
else:
	print s


