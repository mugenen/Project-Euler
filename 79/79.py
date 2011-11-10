
all = set()
a = set()
b = set()
c = set()

f = open("keylog.txt", "r")
for l in f:
	all |= set(list(l.strip()))
	a |= set(list(l.strip()[0]))
	b |= set(list(l.strip()[1]))
	c |= set(list(l.strip()[2]))

print all
print a
print b
print c

#Exclude 4, 5
#BEGIN:7, END:0
#7, 3, 1, 6, 2, 8, 9, 0
#73162890
