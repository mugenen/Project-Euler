import math


class Dice:
	def __init__(self, f, p):
		self.f = f
		self. p = p
	def min(self):
		return self.f
	def max(self):
		return self.f * self.p
	def freq(self, s):
		def comb(n, r):
			if n == 0 or r == 0: return 1
			return comb(n, r - 1) * (n - r + 1) / r
		t = 0
		for i in xrange(0, int(math.floor((s - self.f) / float(self.p))) + 1):
			t += comb(s - self.p * i - 1, self.f - 1) * comb(self.f, i) * (-1) ** i
		
		return t
	def prob(self, s):
		return self.freq(s) / float(self.p ** self.f)
	def range(self):
		return xrange(self.min(), self.max() + 1)


d4 = Dice(9, 4)
d6 = Dice(6, 6)

s = 0
for i in d4.range():
	for j in d6.range():
		if i > j:
			s += d4.prob(i) * d6.prob(j)

math.round(s)


