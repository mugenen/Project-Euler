#http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
def comb(N,k): # from scipy.comb(), but MODIFIED!
    if (k > N) or (N < 0) or (k < 0):
        return 0L
    N,k = map(long,(N,k))
    top = N
    val = 1L
    while (top > (N-k)):
        val *= top
        top -= 1
    n = 1L
    while (n < k+1L):
        val /= n
        n += 1
    return val


import itertools
s = 1
#for i in itertools.count(1):
for i in xrange(1, 101):
	ss = []
	for j in xrange(0, i + 1):
#		print comb(i, j) % 7,
		ss.append(comb(i, j))
	
	t = 0
	for n in ss:
		if n % 7 != 0:
			s += 1
			t += 1
	
	print i + 1, s, t



#‘¬‚¢

s = 1
for n in xrange(1, 100):
	m = 1
	print n + 1,
	while n > 0:
		m *= (n % 7 + 1)
		n /= 7
	
	s += m
	print m, s

print (i + 1) / 2.0 * i, i

s

#‚à‚Á‚Æ‘¬‚¢
#https://github.com/gadial/project-euler/blob/master/problem148.rb

def cal(d):
	l = len(d)
	if l <= 0:
		return 1
	
	w = int(d[0])
	return w * (w + 1) / 2 * 28**(l - 1) + (w + 1) * cal(d[1:])

n = 10 ** 9 - 1
t = []

while n > 0:
	t.append(str(n % 7))
	n /= 7

t.reverse()

d = "".join(t)

cal(d)



