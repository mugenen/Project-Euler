a = 1
b = 2
sum = 0
while b < 4000000:
	sum += b
	a, b = a + 2 * b, 2 * a + 3 * b
sum