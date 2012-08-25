import copy

def triangle(n):
    return n * (n + 1) / 2
def square(n):
    return n * n
def pentagonal(n):
    return n * (3 * n - 1) / 2
def hexagonal(n):
    return n * (2 * n - 1)
def heptagonal(n):
    return n * (5 * n - 3) / 2
def octagonal(n):
    return n * (3 * n - 2)

func = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]

head = []
for i in xrange(6):
    head.append({})

def addNum(i, num):
    num_head = num / 100
    if num_head in head[i]:
        head[i][num_head].append(num)
    else:
        head[i][num_head] = [num]

for n in xrange(1, 200):
    for i, f in enumerate(func):
        f_n = f(n)
        if 1000 <= f_n <= 9999:
            addNum(i, f_n)
        if f_n > 9999:
            break


def search(state, key, visited):
    if len(visited) == 6 and state[0] / 100 == state[-1] % 100:
        print sum(state), state, visited
    for i in xrange(6):
        if i in visited:
            continue
        if key in head[i]:
            for v in head[i][key]:
                if v not in state:
                    state2 = copy.deepcopy(state)
                    visited2 = copy.deepcopy(visited)
                    
                    state2.append(v)
                    visited2.append(i)
                    search(state2, v % 100, visited2)

for v in head[5]:
    for n in head[5][v]:
        state = [n]
        visited = [5]
        search(state, n % 100, visited)

