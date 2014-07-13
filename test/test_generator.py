from passgen.generator import generate
from passgen.charsets import displayable_charset
from passgen.policies import one_letter_one_number

def _test_policy(charset, policy, length):
    password = generate(charset, policy, length=length, urandom=True)
    assert len(password) == length
    for ch in password:
        assert ch in charset
    if policy:
        assert policy.accept(password)

def test_displayable_characters():
    _test_policy(displayable_charset, None, length=10)
    _test_policy(displayable_charset, one_letter_one_number(), length=15)
