from passgen.generator import generate
from passgen.policies import displayable_characters

def _test_policy(policy, length):
    policy = displayable_characters()
    password = generate(policy, length=length, urandom=True)
    assert len(password) == length
    charset = set(policy.allowed_characters())
    for ch in password:
        assert ch in charset

def test_displayable_characters():
    _test_policy(displayable_characters(), length=10)
