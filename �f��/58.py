import itertools
import math
import random

#ミラー・ラビンテスト
#http://d.hatena.ne.jp/pashango_p/20090704/1246692091
def is_prime3(q,k=50):
	q = abs(q)
	#計算するまでもなく判定できるものははじく
	if q == 2: return True
	if q < 2 or q&1 == 0: return False
	
	#n-1=2^s*dとし（但しaは整数、dは奇数)、dを求める
	d = (q-1)>>1
	while d&1 == 0:
		d >>= 1
	
	#判定をk回繰り返す
	for i in xrange(k):
		a = random.randint(1,q-1)
		t = d
		y = pow(a,t,q)
		#[0,s-1]の範囲すべてをチェック
		while t != q-1 and y != 1 and y != q-1: 
			y = pow(y,2,q)
			t <<= 1
		if y != q-1 and t&1 == 0:
			return False
	return True

i = 1
j = 0
ru = 1
s = 0
while True:
	ru += 4 + 4 * i
	if is_prime3(ru - 1 - i):
		s +=1
	if is_prime3(ru- 2 - 2 * i):
		s +=1
	if is_prime3(ru - 3 - 3 * i):
		s +=1
	
	i += 2
	j += 1
#	print s, (4.0 * j) + 1, s / ((4.0 * j) + 1), j
	if s / ((4.0 * j) + 1) < 0.1:
		break

print i

