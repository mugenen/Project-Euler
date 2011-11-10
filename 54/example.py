


def is_flash(sut):
    if len(set(sut)) == 1:
        return True
    return False

def is_st(num):
    if len(set(num)) == 5:
        if ''.join(map(str,sorted(num))) in ''.join((map(str,xrange(1,15)))):     
            return True
    return False 

def is_sf(num,sut):
    if is_flash(sut) and is_st(num):
        return True
    return False

def is_royal(num,sut):
    if is_sf(num,sut) and 14 in num and 10 in num:
        return True
    return False

def is_four(num):
    if len(set(num)) == 2:
        if len(set(sorted(num)[1:-1])) == 1:
            return True
    return False

def is_hou(num):
    if not is_four(num) and len(set(num)) == 2:
        return True
    return False

def is_thr(num):
    if len(set(num)) == 3:
        cnt = 0
        p = sorted(num)[2:-2][0]
        for i in num:
            if p == i:
                cnt += 1
        if cnt == 3:
            return True
    return False

def is_two(num):
    if not is_thr(num) and len(set(num)) == 3:
        return True
    return False

def is_pair(num):
    if len(set(num)) == 4:
        return True
    return False

def rmmax(num):
    g = max(num)
    num.remove(g)
    return g

def rmun(n,num):
    while n in num:
        num.remove(n)

def hand(num,sut):
    if is_royal(num,sut):
        return 15**9
    if is_sf(num,sut):
        g = rmmax(num)
        return 15**8 + g
    if is_four(num):
        g = sorted(num)[2:-2][0]
        rmun(g,num)
        p = rmmax(num)
        return 15**7*g+p
    if is_hou(num):
        x = sorted(num)[2:-2][0]
        rmun(x,num)
        p = num[0]
        rmun(p,num)
        return 15**6*x + p
    if is_flash(sut):
        g = rmmax(num)
        return 15**5+g
    if is_st(num):
        g = rmmax(num)
        return 15**4+g
    if is_thr(num):
        g = sorted(num)[2:-2][0]
        rmun(g,num)
        p = rmmax(num)
        return 15**3*g+p
    if is_two(num):
        g = list(set(num))
        p = [x for x in num]
        for i in g:
            p.remove(i)
        rmun(p[0],num)
        rmun(p[1],num)
        g = rmmax(num)
        return 15**2*p[0] + 15 **2* p[1] + g
    if is_pair(num):
        f = list(set(num))
        p = [x for x in num]
        for i in f:
            p.remove(i)
        rmun(p[0],num)
        g = rmmax(num)
        return 15**1*p[0]+g
    g = rmmax(num)
    return g

def conv(cards):
    lis = []
    for x in cards:
        if x[0] == 'K':
            lis.append(13)
        elif x[0] == 'A':
            lis.append(14)
        elif x[0] == 'Q':
            lis.append(12)
        elif x[0] == 'J':
            lis.append(11)
        elif x[0] == 'T':
            lis.append(10)
        else:
            lis.append(int(x[0]))
    return lis

cnt = 0
for line in open('poker.txt'):
    cards = line.rstrip().split(' ')
    play1 = cards[:5]
    num1 = conv(play1)
    sui1 =[x[1] for x in play1]
    play2 = cards[5::]
    num2 = conv(play2)
    sui2 = [x[1] for x in play2]
    x = hand(num1,sui1)
    y = hand(num2,sui2)
    if x > y:
        cnt += 1
        print "WIN", play1, play2
    elif x == y:
        print x,y
        while len(num1) and len(num2):
            p = rmmax(num1)
            q = rmmax(num2)
            if p > q:
                cnt += 1
                print "WIN", play1, play2
                break
    if not len(num1) and not len(num2):
        print 'draw'

print cnt