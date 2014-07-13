import string

_DISPLAYABLE = string.digits + string.letters + string.punctuation + ' '

class displayable_characters(object):
    def allowed_characters(self):
        return _DISPLAYABLE
