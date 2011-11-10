import csv

def isInner(ax, ay, bx, by, cx, cy):
	t1 = bx * ay - ax * by
	t2 = cx * by - bx * cy
	t3 = ax * cy - cx * ay
	if t1 > 0 and t2 > 0 and t3 > 0 or t1 < 0 and t2 < 0 and t3 < 0:
		return 1
	else:
		return 0

f = open("triangles.txt")

r = csv.reader(f)
s = 0
for w in r:
	w = [int(i) for i in w]
	s += isInner(w[0], w[1], w[2], w[3], w[4], w[5])

f.close()
print s
