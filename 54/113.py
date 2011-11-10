#http://topcoder.g.hatena.ne.jp/delta2323/20110531/1306800560
def comb(N,k): # from scipy.comb(), but MODIFIED!
    if (k > N) or (N < 0) or (k < 0):
        return 0L
    N,k = map(long,(N,k))
    top = N
    val = 1L
    while (top > (N-k)):
        val *= top
        top -= 1
    n = 1L
    while (n < k+1L):
        val /= n
        n += 1
    return val


comb(109, 9) + comb(110, 10) - 10 * 100 - 2
