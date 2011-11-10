import csv

f = open("matrix.txt", "r")

LEN = 80
mat = [[0] * (LEN + 2) for x in xrange((LEN + 2))]
score = [[0] * (LEN + 2) for x in xrange((LEN + 2))]

for i in xrange(1, LEN + 1):
	mat[0][i] = 1000000000
	mat[LEN + 1][i] = 1000000000
r = csv.reader(f)

i = 1
for row in r:
	j = 1
	for n in row:
		mat[i][j] = int(n)
		j += 1
	i += 1

f.close()

q = []

for i in xrange(1, LEN + 1):
	q.append((i, 1, mat[i][1]))

q.sort(lambda x, y: x[2] - y[2])
while True:
	t = q.pop(0)
	if score[t[0]][t[1]] == 1:
		continue
	if t[1] == LEN + 1:
		print t
		break
	print t
	score[t[0]][t[1]] = 1
	q.append((t[0] + 1, t[1], t[2] + mat[t[0] + 1][t[1]]))
	print (t[0] + 1, t[1], t[2] + mat[t[0] + 1][t[1]]), (t[0] - 1, t[1], t[2] + mat[t[0] - 1][t[1]]), (t[0], t[1] + 1, t[2] + mat[t[0]][t[1] + 1])
	q.append((t[0] - 1, t[1], t[2] + mat[t[0] - 1][t[1]]))
	q.append((t[0], t[1] + 1, t[2] + mat[t[0]][t[1] + 1]))
	q.sort(lambda x, y: x[2] - y[2])

