import itertools

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
        
        print top, last, s, flag
        
        if s == 0 and flag:
            break
        
        enum += last - top
        flag = True

print enum