import csv
import itertools

f = open("cipher1.txt", "r")
b = ord('a')
probable = []
num = []
for row in csv.reader(f):
	for c in row:
		num.append(int(c))

for key in xrange(26):
	key += b
	success = True
	for c in num:
		c ^= key
		if(c > 176 or c < 32):
			success = False
			break
	if success:
		probable.append(key)

m = 0
ans = ""
for key in itertools.product(probable, repeat = 3):
	count = 0
	temp = num[:]
	for i in xrange(len(num)):
		if i % 3 == 0:
			temp[i] ^= key[0]
		if i % 3 == 1:
			temp[i] ^= key[1]
		if i % 3 == 2:
			temp[i] ^= key[2]
		if chr(temp[i]) == ' ':
			count += 1
	if count > m:
		m = count
		ans = key

print [chr(k) for k in ans]

s = 0
for i in xrange(len(num)):
	if i % 3 == 0:
		num[i] ^= ans[0]
	if i % 3 == 1:
		num[i] ^= ans[1]
	if i % 3 == 2:
		num[i] ^= ans[2]
	print chr(num[i]),
	s += num[i]

print s
f.close()
