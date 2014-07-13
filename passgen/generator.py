from sampler import sample

def generate(charset, policy, length, urandom=False):
    assert length > 0
    n = len(charset)
    fname = '/dev/urandom' if urandom else '/dev/random'
    with open(fname) as f:
        while 1:
            password = ''.join(charset[sample(n, f)] for _ in xrange(length))
            if policy is None or policy.accept(password):
                return password
