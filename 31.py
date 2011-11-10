M = [1, 2, 4, 10, 20, 40, 100]
import itertools
s = 0
for i0 in xrange(M[0], -1, -1):
	for i1 in xrange(M[1], -1, -1):
		if 200 * i0 + 100 * i1 > 200:
			continue
		for i2 in xrange(M[2], -1, -1):
			if 200 * i0 + 100 * i1 + 50 * i2> 200:
				continue
			for i3 in xrange(M[3], -1, -1):
				if 200 * i0 + 100 * i1 + 50 * i2 + 20 * i3> 200:
					continue
				for i4 in xrange(M[4], -1, -1):
					if 200 * i0 + 100 * i1 + 50 * i2 + 20 * i3 + 10 * i4> 200:
						continue
					for i5 in xrange(M[5], -1, -1):
						if 200 * i0 + 100 * i1 + 50 * i2 + 20 * i3 + 10 * i4 + 5 * i5> 200:
							continue
						for i6 in xrange(M[6], -1, -1):
							if 200 * i0 + 100 * i1 + 50 * i2 + 20 * i3 + 10 * i4 + 5 * i5 + 2 * i6> 200:
								continue
							else:
								s += 1

print s

73682
