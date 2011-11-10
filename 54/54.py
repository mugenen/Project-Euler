import collections
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
def result(s):
	r = ["HIGH", "ONE", "TWO", "THREE", "STRAIGHT", "FLUSH","FULL", "FOUR", "STFL", "ROYAL"]
	if s <= 13:
		return s
	else:
		return r[s - 13]

def score(x):
	p1n = collections.Counter()
	p1s = collections.Counter()
	for c in x:
		p1n[c[0]] += 1
		p1s[c[1]] += 1
	
	straight = -1
	ss = 0
	for i in xrange(13 - 5):
		ss = 0
		for j in xrange(5):
			if cards[i + j] in p1n:
				ss += 1
		if ss == 5:
			straight = i
			break
	m = -1
	for i in xrange(12, -1, -1):
		if p1n[cards[i]] == max(p1n.values()):
			m = i
			break
	
	if len(p1n) == 2:
		if max(p1n.values()) == 4:#FourCards
			return 20, m + 1
		else:#FullHouse
			return 19, m + 1
	elif len(p1s) == 1:#Flash
		if straight != -1:
			if straight == 8:#Royal
				return 22, m + 1
			else:#Straight
				return 21, m + 1
		else:
			return 18, m + 1
	else:
		if straight != -1:
			return 17, m + 1
		elif len(p1n) == 3:
			if max(p1n.values()) == 3:
				return 16, m
			else:
				return 15, m
		elif len(p1n) == 4:
			return 14, m + 1
		else:
			return m + 1, m + 1

with open("poker.txt", "r") as f:
	s = 0
	for l in f:
		p = l.split()
		p1, a = score(p[:5])
		p2, b = score(p[5:])
		if p1 > p2:
			s += 1
			print result(p1), result(p2), "WIN", p[:5], p[5:]
		elif p1 == p2 and a > b:
			s += 1
			print result(p1), result(p2), "WIN", p[:5], p[5:]
#		else:
#			print result(p1), result(p2), a, b, "LOSE", p[:5], p[5:]
	print s
