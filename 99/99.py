import math
import csv

f = open("base_exp.txt", "r")
m = 0
i = 0
for l in csv.reader(f):
	i += 1
	d = int(l[1]) * math.log(int(l[0]))
	if m < d:
		m = d
		print i

f.close()
