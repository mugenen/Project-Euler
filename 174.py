import itertools
import collections

MAX = 1000000

odd = []
even = []

for i in itertools.count(3, 2):
    if 4 * i - 4 > MAX:
        break
    
    odd.append(4 * i - 4)

for i in itertools.count(4, 2):
    if 4 * i - 4 > MAX:
        break
    even.append(4 * i - 4)


q = collections.Counter()
enum = 0
for num in [odd, even]:
    s = 0
    top = 0
    last = 0
    count = 0
    flag = False
    
    while True:
        if s != 0:
            s -= num[top]
            top += 1
        
        for o in num[last:]:
            temp = s + o
            if temp > MAX:
                break
        
            s = temp
            last += 1
        
#        print top, last, s, flag
        
        if s == 0 and flag:
            break
        
        enum += last - top
        flag = True
        z = 0
        for t in num[top:last]:
            z += t
            q[z] += 1

print enum

zz = collections.Counter()
for qq in q:
    zz[q[qq]] += 1

print zz[1] + zz[2] + zz[3] + zz[4] + zz[5] + zz[6] + zz[7] + zz[8] + zz[9] +zz[10]
