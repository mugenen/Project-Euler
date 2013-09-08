import bisect

#MAX = 100000001
MAX = 100000001
prime = [-1] * MAX
i = 2
p = set()
while MAX > i:
    if prime[i - 1] == -1:
        prime[i - 1] = 0
        p.add(i)
        temp = i * 2
        while temp < MAX:
            prime[temp - 1] = 1
            temp += i
    if i == 2:
        i += 1
    else:
        i += 2

MAX -= 1

prime = [-1] * MAX
i = 2
while MAX > i:
    if prime[i - 1] == -1:
        prime[i - 1] = 0
        temp = i * 2
        while temp < MAX:
#            print i, temp, (i + temp / i)
#            if prime[temp - 1] != 1 and (i + temp / i) in p:
            if prime[temp - 1] != 1 and (i + temp / i) in p and (1 + temp) in p:
                prime[temp - 1] = 2
            else:
                prime[temp - 1] = 1
            temp += i
    if i == 2:
        i += 1
    else:
        i += 2

result = 3
for i in xrange(MAX):
    if prime[i] == 2:
#        print i + 1
        result += i + 1

print result
