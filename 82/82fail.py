import csv

f = open("matrix.txt", "r")

r = csv.reader(f)
LEN = 80
mat = [[100000000] * (LEN + 2) for x in xrange((LEN + 2))]

i = 1
for row in r:
	j = 1
	for n in row:
		mat[i][j] = int(n)
		j += 1
	i += 1

result = {}
def cost(i, j):
	if (i, j) in result:
		return result[(i, j)]
#	if j == 1:
#		result[(i, j)] = mat[i][j]
#		return mat[i][j]
	if j <= 0 or j > LEN or i <= 0 or i > LEN:
		result[(i, j)] = 0
		return 0
	ans = min(cost(i - 1, j - 1) + mat[i - 1][j] + mat[i][j], cost(i, j - 1) + mat[i][j], cost(i + 1, j - 1) + mat[i + 1][j] + mat[i][j])
	result[(i, j)] = ans
	return ans

f.close()

ret = []
for i in xrange(1, LEN + 1):
	ret.append(cost(i, LEN))

print min(ret)
