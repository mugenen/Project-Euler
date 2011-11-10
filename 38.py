for i in xrange(9999, 1, -1):
	ll = []
	ls = set()
	flag = False
	for j in xrange(1, 10):
		st = str(i * j)
		ll.extend(st)
		ls |= set(st)
		if len(ll) > 9:
			break
		if len(ll) == 9 and len(ls) == 9 and "0" not in ls:
			flag = True
			break
	if flag:
		print i, ll, ls, "".join(ll)
		break
