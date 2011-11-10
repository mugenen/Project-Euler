n(x + y) = xy
n = xy / x + y
y ‚Í n ‚Ìq ”{

3

y = ne

x + ne = xe
x(e - 1) = ne
x = ne / (e - 1)

import itertools
for n in xrange(180180, 180181):
	s = 0
	for e in xrange(2, n + 2):
		if n % (e - 1) == 0:
			s += 1
#			print n * e / (e - 1)
	
	print n, s
	if s >= 1000:
		break

#n‚Ì–ñ”‚ÌŒÂ”‚É“™‚µ‚¢

MAX = 100000000

div = [0] * MAX

for i in xrange(1, MAX):
	for j in xrange(i, MAX, i):
		div[j] += 1


s = 0
for i in xrange(2, 10000000 - 1):
	if div[i] >= 1000:
		print i
		break


Upper Bound:2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29
##ŠÔˆá‚Á‚Ä‚½n^2‚Ì–ñ”‚ª1999ŒÂˆÈã‚É‚È‚ê‚Î‚¢‚¢
#http://d.hatena.ne.jp/lpocean0722/20080701/1214931511
Upper Bound:2 * 3 * 5 * 7 * 11 * 13 * 17
ANSWER:2 * 3 * 5 * 7 * 11 * 13 * 2 * 3