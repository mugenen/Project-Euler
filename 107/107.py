import csv

entire = 0
result = 0
edge = []
#read upper triangle matrix
with open("network.txt") as f:
	r = 0
	for row in csv.reader(f):
		c = 0
		for item in row:
			if item != "-" and c >= r:
				temp = int(item)
				entire += temp
				edge.append((r, c, temp))
			c += 1
		r += 1


#sort edges by weight
edge.sort(lambda x, y: x[2] - y [2])

tree = [set([i]) for i in xrange(r)]

while len(tree[0]) < r and len(edge) > 0:
	#add edge connecting different trees
#	print edge[0], len(edge), tree
	tree1 = tree[edge[0][0]]
	tree2 = tree[edge[0][1]]
	if tree1 != tree2:
		result += edge[0][2]
		newtree = tree1 | tree2
		for v in newtree:
			tree[v] = newtree
	
	edge.pop(0)
	
print entire, result, entire - result