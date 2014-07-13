def str2int(s):
    n = 0
    for i, ch in enumerate(s):
        n += (ord(ch) << i)
    return n

def sample(n, r):
    """
    Generate a random integer from [0, n), where n > 0
    """

    assert n > 0

    # find x, the smallest power of 2 such that n <= x
    x = 2
    bits = 1
    while x < n:
        x <<= 1
        bits += 1
    assert n <= x
    bytes = (bits / 8 + 1) if bits % 8 else (bits / 8)

    # rejection sample on random integers from [0, x)
    while 1:
        rng = str2int(r.read(bytes))
        rng = rng % x
        if rng < n:
            return rng
