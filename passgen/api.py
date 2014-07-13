from generator import generate_variable
from charsets import displayable_charset, amex_charset
from policies import one_letter_one_number, \
        does_not_start_with, does_not_end_with, pipeline

import limits
import string

class api(object):
    def __init__(self, charset, policy, min_length, max_length):
        self._charset = charset
        self._policy = policy
        self._min_length = min_length
        self._max_length = max_length

    def generate(self, urandom=False):
        return generate_variable(self._charset, self._policy,
                self._min_length, self._max_length, urandom)

class google(api):
    def __init__(self,
                 min_length=limits.google[0],
                 max_length=limits.google[1]):
        super(google, self).__init__(
                displayable_charset, None, min_length, max_length)

class amex(api):
    def __init__(self,
                 min_length=limits.amex[0],
                 max_length=limits.amex[1]):
        super(amex, self).__init__(
                amex_charset, one_letter_one_number(), min_length, max_length)

class boa(api):
    def __init__(self,
                 min_length=limits.boa[0],
                 max_length=limits.boa[1]):
        p = pipeline([
            one_letter_one_number(),
            does_not_start_with(string.digits),
            does_not_end_with(string.digits),
        ])
        super(boa, self).__init__(amex_charset, p, min_length, max_length)
