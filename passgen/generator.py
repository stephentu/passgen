from sampler import sample

import logging
logger = logging.getLogger(__name__)

def generate(charset, policy, length, urandom=False):
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
