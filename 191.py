import itertools

N = 30

state = [[1, 1], [1, 0], [0, 0]]
for i in xrange(N - 1):
    new_state = [[0, 0], [0, 0], [0, 0]]
    
    new_state[0][0] = state[0][0] + state[1][0] + state[2][0]
    new_state[0][1] = state[0][0] + state[0][1] + state[1][0] + state[1][1] + state[2][0] + state[2][1]
    new_state[1][0] = state[0][0]
    new_state[1][1] = state[0][1]
    new_state[2][0] = state[1][0]
    new_state[2][1] = state[1][1]
    
    state = new_state

#    print state
print sum(map(sum, state))
