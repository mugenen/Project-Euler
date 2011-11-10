
import itertools

i = 10 ** 7
while True:
	x = i
	x *= 10
	x += 7
	x *= 10
	x = x ** 2
	st = str(x)
	if len(st) == 19 and st[16] == '9' and st[14] == '8' and st[12] == '7' and st[10] == '6' and st[8] == '5' and st[6] == '4' and st[4] == '3' and st[2] == '2':
		print st, (i * 10 + 7) * 10
		break
	i += 1
	

