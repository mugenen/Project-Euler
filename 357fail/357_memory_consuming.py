import bisect

#MAX = 100000001
MAX = 100001
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

P = len(p)

partial_sum = [[0 for i in xrange(P)] for j in xrange(P)]

for i in xrange(P):
    p_sum = 0
    for j in xrange(i, P):
        p_sum += p[j]
        partial_sum[i][j] = p_sum

result = [2]
temp = [2]

def dfs(last, temp, mult):
    for i in xrange(last + 1, P):
        new_mult = mult * p[i]
        if new_mult < MAX:
            if i + 1 < P and new_mult * p[i + 1] < MAX:
                temp.append(p[i])
                dfs(i, temp, new_mult)
                result[0] += new_mult
                print new_mult, temp
                temp.pop()
            else:
                rest = MAX / mult
                index = bisect.bisect_right(p, rest, i) - 1
                result[0] += mult * partial_sum[i][index]
                print p[index], mult, rest, p[index] * new_mult
                break

dfs(0, temp, 2)
print result[0]
