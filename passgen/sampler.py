import numpy as np
import logging

logger = logging.getLogger(__name__)

def str2int(s):
    n = 0
    for i, ch in enumerate(s):
        n += (ord(ch) << (i*8))
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


def sample_uniform_01(r):
    """
    Generate a random float between [0, 1)
    """
    bytes = 8
    return float(str2int(r.read(bytes))) / float(1 << bytes*8)

def scores_to_probs(scores):
    """
    Adapted from:
    https://github.com/forcedotcom/distributions/blob/7b65f29687e4bd4697717d059ae98f1408a0b538/distributions/util.py#L33
    """
    scores = np.array(scores)
    scores -= scores.max()
    probs = np.exp(scores, out=scores)
    probs /= probs.sum()
    return probs

def sample_discrete_log(scores, r):
    """
    Adapted from:
    https://github.com/forcedotcom/distributions/blob/c8084f8ef6269cc9eef4a4ade9a9219ffde056d1/distributions/dbg/random.py#L59
    """
    probs = scores_to_probs(scores)
    return sample_discrete(probs, total=1.0, r=r)

def sample_discrete(probs, total, r):
    """
    Draws from a discrete distribution with the given (possibly unnormalized)
    probabilities for each outcome.

    Returns an int between 0 and len(probs)-1, inclusive

    Adapted from:
    https://github.com/forcedotcom/distributions/blob/c8084f8ef6269cc9eef4a4ade9a9219ffde056d1/distributions/dbg/random.py#L68
    """
    if total is None:
        total = float(sum(probs))
    for attempt in xrange(10):
        dart = sample_uniform_01(r) * total
        for i, prob in enumerate(probs):
            dart -= prob
            if dart <= 0:
                return i
    logger.error(
        'imprecision in sample_discrete',
        dict(total=total, dart=dart, probs=probs))
    raise ValueError('\n  '.join([
        'imprecision in sample_discrete:',
        'total = {}'.format(total),
        'dart = {}'.format(dart),
        'probs = {}'.format(probs),
    ]))
