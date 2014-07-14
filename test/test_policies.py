from passgen.policies import \
    repeated_letters_or_digits, \
    consecutive_digits

def test_repeated_letters_or_digits():
    p = repeated_letters_or_digits(6)
    assert p.accept('11111')
    assert p.accept('baaaaa')
    assert not p.accept('asdf222222')
    assert not p.accept('asdf3333333')
    assert not p.accept('asdfaaaaaaaab')

def test_consecutive_digits():
    p = consecutive_digits(6)
    assert p.accept('12345')
    assert p.accept('54321')
    assert p.accept('76548')
    assert not p.accept('123456')
    assert not p.accept('987654')
