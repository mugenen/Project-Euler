代名詞の性別
	微妙


属性で関係を推定できそうか？
名詞など

人物リストを学習リソースにするとか
	単語の抽出に使うとか……

3n^2 - n + 3 (n - d)^2 - n + d 
= 6n ^2 - 2n - 6nd + 3d^2 + d
=3(sqrt(2)n - d)^2 + 6sqrt(2)nd - 6 nd - 2n +d






#pentagonal = []
#for i in xrange(1, 10000):
#	n = i * (3 * i - 1) / 2
#	pentagonal.append(n)
#
#for i in xrange(len(pentagonal)):
#	for j in xrange(i + 1, len(pentagonal)):
#		diff = pentagonal[j] - pentagonal[i]
#		add = pentagonal[i] + pentagonal[j]
#		if diff in pentagonal and add in pentagonal:
#			print diff, i, j

#諦めて答えを見た
#http://tsumuji.cocolog-nifty.com/tsumuji/2009/04/project-euler-5.html

import itertools
import math

def pentagon(q):
	x = (1 + math.sqrt(1 + 24 * q)) / 6.0
	return int(x) == x

pentagonal = []


for i in itertools.count(1):
	print i, n
	n = i * (3 * i - 1) / 2
	f = False
	for m in pentagonal:
		diff = n - m
		add = n + m
		if pentagon(diff) and pentagon(add):
			print diff, n, m
			f = True
			break
	pentagonal.insert(0, n)
	if f:
		break





