import csv

f = open("matrix.txt", "r")

r = csv.reader(f)
LEN = 80
mat = [[10000000] * (LEN + 1) for x in xrange((LEN + 1))]

i = 1
for row in r:
	j = 1
	for n in row:
		mat[i][j] = int(n)
		j += 1
	i += 1

score = [[0] * (LEN + 1) for x in xrange(LEN + 1)]

def ps():
	for i in xrange(0, (LEN + 1)):
		for j in xrange(0, (LEN + 1)):
			print score[i][j],
		print


for i in xrange(1, (LEN + 1)):
	for j in xrange(1, (LEN + 1)):
		if i == 1:
			score[i][j] = score[i][j - 1] + mat[i][j]
		elif j == 1:
			score[i][j] = score[i - 1][j] + mat[i][j]
		else:
			score[i][j] = min(score[i - 1][j] + mat[i][j], score[i][j - 1] + mat[i][j])

f.close()
ps()
