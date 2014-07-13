from sampler import sample, sample_discrete
from util import logsumexp, almost_equals

import numpy as np
import logging

logger = logging.getLogger(__name__)

def generate0(charset, policy, length, f):
    n = len(charset)
    while 1:
        password = ''.join(charset[sample(n, f)] for _ in xrange(length))
        logger.debug("generated password: {}".format(password))
        if policy is None or policy.accept(password):
            return password
        logger.debug("rejected password: {}".format(password))

def generate(charset, policy, length, urandom):
    assert length > 0
    fname = '/dev/urandom' if urandom else '/dev/random'
    with open(fname) as f:
        return generate0(charset, policy, length, f)

def generate_variable(charset, policy, min_length, max_length, urandom):
    """
    min_length, max_length inclusive
    """
    assert min_length > 0
    assert min_length <= max_length
    n = len(charset)
    choices = np.arange(min_length, max_length + 1)
    scores = choices * np.log(n)
    scores -= logsumexp(scores)
    probs = np.exp(scores)
    assert almost_equals(probs.sum(), 1.0)

    fname = '/dev/urandom' if urandom else '/dev/random'
    with open(fname) as f:
        choice = choices[sample_discrete(probs, total=1.0, r=f)]
        return generate0(charset, policy, choice, f)
