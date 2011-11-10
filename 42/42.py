import csv
read = csv.reader(file("words.txt", "r"),)

tri = []
for i in xrange(1, 20):
	tri.append(i*(i + 1) / 2)
s = 0
for row in read:
	for word in row:
		ss = 0
		for c in word:
			ss += ord(c) - ord("A") + 1
		if ss in tri:
			s += 1
#			print ss, tri

print s
