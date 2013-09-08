#http://d.hatena.ne.jp/rg350/20101223/1293090603
result = 2

num0 = 0
num1 = 1

limit = 30

assert limit > 2

for i in xrange(limit - 1):
    num0, num1 = num0 + num1, num0
    result += num0
    result += num1
#    print num0, num1

print result
