import string
import re

"""
policies define certain business logic that a password must satisfy. examples
include:
    * at least one letter and number
"""

class one_letter_one_number(object):
    """
    examples:
        * american express
    """
    def accept(self, password):
        digits = set(string.digits)
        letters = set(string.letters)
        digit_test = bool([1 for ch in password if ch in digits])
        letter_test = bool([1 for ch in password if ch in letters])
        return digit_test and letter_test

class does_not_start_with(object):
    def __init__(self, blacklist):
        self._blacklist = set(blacklist)

    def accept(self, password):
        return password[0] not in self._blacklist

class does_not_end_with(object):
    def __init__(self, blacklist):
        self._blacklist = set(blacklist)

    def accept(self, password):
        return password[-1] not in self._blacklist

class repeated_letters_or_digits(object):
    """
    Reject passwords with length or more consecutive repeated letters/digits
    (or some subset)
    """
    def __init__(self, length, chars=string.digits+string.letters):
        digits = set(string.digits)
        letters = set(string.letters)
        for ch in chars:
            if ch not in digits and ch not in letters:
                # XXX: lazy; don't want to bother escaping regexes
                # XXX: FIXME
                raise ValueError("impl limitation")
        if length <= 0:
            raise ValueError("bad length")
        self._chars = chars
        self._regex = re.compile('|'.join('%s{%d}' % (ch, length) for ch in self._chars))
        self._length = length

    def accept(self, password):
        if self._regex.search(password):
            return False
        return True

class consecutive_digits(object):
    """
    Reject passwords containing some (>= length) substring of "0123456789" or
    "9876543210"
    """
    def __init__(self, length):
        if length <= 0 or length >=10:
            raise ValueError("impossible length")
        self._length = length
    def accept(self, password):
        # XXX: not a very optimal implementation
        digits = '0123456789'
        reverse_digits = digits[::-1]
        for i in xrange(len(digits)):
            substr = digits[i:i+self._length]
            if len(substr) != self._length:
                continue
            if password.find(substr) != -1:
                return False
            substr = reverse_digits[i:i+self._length]
            if password.find(substr) != -1:
                return False
        return True

class pipeline(object):
    def __init__(self, policies):
        self._policies = policies

    def accept(self, password):
        for policy in self._policies:
            if not policy.accept(password):
                return False
        return True
