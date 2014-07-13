import string

"""
policies define certain business logic that a password must satisfy. examples
include:
    * at least one letter and number
"""

class one_letter_one_number(object):
    """
    eaxmples:
        * american express
    """
    def accept(self, password):
        digits = set(string.digits)
        letters = set(string.letters)
        digit_test = bool([1 for ch in password if ch in digits])
        letter_test = bool([1 for ch in password if ch in letters])
        return digit_test and letter_test
