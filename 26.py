def prime(n):
	p = {}
	def add(i):
		if i in p:
			p[i] += 1
		else:
			p[i] = 1
	i = 2
	while i <= n:
		if n % i == 0:
			n = n / i
			add(i)
		else:
			if i != 2:
				i += 2
			else:
				i += 1
	return p

m = 0
for i in xrange(1, 1001):
	t = prime(i)
	if len(t) > 0:
		m = max(m, max(t))

m


‚Å‚È‚¢
#http://ja.wikipedia.org/wiki/%E5%BE%AA%E7%92%B0%E5%B0%8F%E6%95%B0



#http://d.hatena.ne.jp/likr/20100125

def cycle(n):
	while n % 2 == 0:
		n /= 2
	while n % 5 == 0:
		n /= 5
	if n == 1:
		return 0
	count = 1
	while 10**count % n != 1:
		count += 1
	return count

m = 0
mm = 0
for i in xrange(1, 1001):
	p = prime(i)
	if len(p) == 1:
		mp = max(p)
		mc = cycle(mp)
		if mc > mm:
			mm = mc
			m = mp

m
