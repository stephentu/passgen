import string

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

class pipeline(object):
    def __init__(self, policies):
        self._policies = policies

    def accept(self, password):
        for policy in self._policies:
            if not policy.accept(password):
                return False
        return True
