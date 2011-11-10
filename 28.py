sum = 1

i = 1
ru = 1
while i < 1001:
	ru += 4 + 4 * i
	sum += ru
	sum += ru - 1 - i
	sum += ru - 2 - 2 * i
	sum += ru - 3 - 3 * i
#	print ru, ru - 1 - i, ru - 2 - 2 * i, ru - 3 - 3 * i, sum
	i += 2

sum

669171001
