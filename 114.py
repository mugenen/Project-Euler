memo ={}
def cal(n):
	if n <= 0:
		return 1
	if n in memo:
		return memo[n]
	s = 1
	for i in xrange(0, n - 2):
		for j in xrange(i + 3, n + 1):
			s += cal(n - j - 1)
	memo[n] = s
	return s

#http://topcoder.g.hatena.ne.jp/delta2323/20110628/1309217127
#‚È‚ñ‚Ån-j‚©‚ç1ˆø‚­‚Ì‚©‚í‚©‚ç‚È‚¢
