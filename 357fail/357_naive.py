#MAX = 100000001
MAX = 10001
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

result = [2]
temp = [2]

def dfs(last, temp, mult):
    for i in xrange(last + 1, P):
        new_mult = mult * p[i]
        if new_mult < MAX:
            temp.append(p[i])
            dfs(i, temp, new_mult)
            result[0] += new_mult
            print new_mult, temp
            temp.pop()

dfs(0, temp, 2)
print result[0]
