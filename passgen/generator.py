from sampler import sample

def generate(policy, length, urandom=False):
    assert length > 0
    charset = policy.allowed_characters()
    n = len(charset)
    fname = '/dev/urandom' if urandom else '/dev/random'
    with open(fname) as f:
        return ''.join(charset[sample(n, f)] for _ in xrange(length))
