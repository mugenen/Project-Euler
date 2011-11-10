#http://d.hatena.ne.jp/jeneshicc/20081117/1226925289
with open("roman.txt") as f:
	s = 0
	for line in f:
		line = line.strip()
		L = len(line)
		n = 0
		rep = [("DD","M"),("CCCCC","D"),("LL","C"),("XXXXX","L"),("VV","X"),("IIIII","V"), ("DCCCC","CM"),("CCCC","CD"),("LXXXX","XC"),("XXXX","XL"),("VIIII","IX"),("IIII","IV")]
		for q, d in rep:
			line = line.replace(q, d)
		C = len(line)
		s += L - C
	else:
		print s
