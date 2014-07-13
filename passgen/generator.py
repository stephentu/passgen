from sampler import sample
from util import logsumexp

import numpy as np
import logging

logger = logging.getLogger(__name__)

def generate(charset, policy, length, urandom):
    assert length > 0
    n = len(charset)
    fname = '/dev/urandom' if urandom else '/dev/random'
    with open(fname) as f:
        while 1:
            password = ''.join(charset[sample(n, f)] for _ in xrange(length))
            logger.debug("generated password: {}".format(password))
            if policy is None or policy.accept(password):
                return password
            logger.debug("rejected password: {}".format(password))

def generate_variable(charset, policy, min_length, max_length, urandom):
    """
    min_length, max_length inclusive
    """
    assert min_length > 0
    assert min_length <= max_length
    n = len(charset)
    scores = np.arange(min_length, max_length+1) * np.log(n)
    scores -= logsumexp(scores)
    probs = np.exp(scores)
