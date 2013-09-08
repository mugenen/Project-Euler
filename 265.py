import collections
N = 5

candidate = []
next = collections.defaultdict(set)

for i in xrange(0, 32):
    candidate.append(bin(i)[2:].zfill(N))
    next[candidate[-1][:-1]].add(candidate[-1])


START = '0' * N
result = [0]
visited = set([START])
route = [START]

def dfs(last, visited, route):
    if len(visited) == 2 ** N:
        print route,
        num = route[0]
        for i in xrange(1, len(route) - N + 1):
            num += route[i][-1]
        print int(num, 2)
        result[0] += int(num, 2)
        return
    for n in next[last[1:]]:
        if n not in visited:
            visited.add(n)
            route.append(n)
            dfs(n, visited, route)
#            print route
            visited.remove(n)
            route.pop()

dfs(START, visited, route)

print result[0]
