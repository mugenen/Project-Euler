import Queue
import math

p = []
N = 10000
mx = 4 * 10**6
q = Queue.PriorityQueue()
q.put((2,[1]))
INF = 10000000

def isprime(n):
    if (n == 0 or n == 1):
        return False
    for i in xrange(2,int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True

def sieve(n):
    for i in xrange(n):
        if(isprime(i)):
            p.append(i)

def calc(powlist):
    return (reduce(lambda x,y:x*y ,map(lambda x:2*x+1 , powlist),1) + 1)/2

def add_one(list):
    list.sort()
    list.reverse()
    ret = []
    if(len(list) == 1 or (len(list) >= 2 and list[-1] < list[-2]) ):
        buf = copy.copy(list)
        buf[-1] += 1
        ret.append(buf)
    list.append(1)
    ret.append(list)
    return ret

def makeval(list):
    return reduce(lambda a,b :a*b , map( lambda (a,r) :a**r , zip(p[0:len(list)], list)),1 )

sieve(N)
while(True):
    val, powlist = q.get()
    if(calc(powlist) > mx):
        print val
        break
    else:
        for newpowlist in add_one(powlist):
            q.put((makeval(newpowlist) , newpowlist))

#
#http://topcoder.g.hatena.ne.jp/delta2323/20110328/1301298909

import Queue
import math
import itertools

MAX = 10000
prime = [-1] * MAX
i = 2
p = []
while MAX > i:
	if prime[i - 1] == -1:
		prime[i - 1] = 0
		p.append(i)
		temp = i * 2
		while temp < MAX:
			prime[temp - 1] = 1
			temp += i
	if i == 2:
		i += 1
	else:
		i += 2


N = 10000
mx = 4 * 10**6
q = Queue.PriorityQueue()
q.put((2,[1]))
INF = 10000000

def div(list):
	return (reduce(lambda x,y:x*y ,map(lambda x:2*x+1 , powlist),1) + 1)/2



def val(list):
	return reduce(lambda a,b :a*b , map( lambda (a,r) :a**r , zip(p[0:len(list)], list)),1)

def add_one(list):
    list.sort()
    list.reverse()
    ret = []
    if(len(list) == 1 or (len(list) >= 2 and list[-1] < list[-2]) ):
        buf = list[:]
        buf[-1] += 1
        ret.append(buf)
    list.append(1)
    ret.append(list)
    return ret


while(True):
	v, powlist = q.get()
	if(div(powlist) > mx):
		print v
		break
	else:
		for newpowlist in add_one(powlist):
			q.put((val(newpowlist) , newpowlist))
