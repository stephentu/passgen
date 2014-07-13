from generator import generate
from charsets import displayable_charset, amex_charset
from policies import one_letter_one_number, \
        does_not_start_with, does_not_end_with, pipeline

import limits
import string

class api(object):
    def __init__(self, charset, policy, limit):
        self._charset = charset
        self._policy = policy
        self._limit = limit

    def generate(self, urandom=False):
        return generate(self._charset, self._policy, self._limit, urandom)

class google(api):
    def __init__(self, limit=limits.google[1]):
        super(google, self).__init__(displayable_charset, None, limit)

class amex(api):
    def __init__(self, limit=limits.amex[1]):
        super(amex, self).__init__(amex_charset, one_letter_one_number(), limit)

class boa(api):
    def __init__(self, limit=limits.boa[1]):
        p = pipeline([
            one_letter_one_number(),
            does_not_start_with(string.digits),
            does_not_end_with(string.digits),
        ])
        super(boa, self).__init__(amex_charset, p, limit)
