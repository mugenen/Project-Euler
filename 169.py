#http://d.hatena.ne.jp/inamori/20121102/p1
#http://d.hatena.ne.jp/inamori/20121103/p1

n = 10**25

a = 1
b = 0
while n > 0:
    if n & 1 == 1:
        a = a + b
    else:
        b = a + b
    n >>= 1