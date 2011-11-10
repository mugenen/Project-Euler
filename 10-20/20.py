reduce(lambda x, y: int(x) + int(y), str(reduce(lambda x, y: x * y, xrange(1, 101))))
