N = 1000000001
phi = range(2, N)
for i in xrange(2, N):
    if phi[i - 2] == i:
        for j in xrange(i - 2, len(phi), i):
            phi[j] = phi[j] * float(i - 1) / i

for i in xrange(2, N):
#    print phi[i - 2], t, i
    if phi[i - 2] / (i - 1) < 15499.0/94744:
        print i

#892371480
