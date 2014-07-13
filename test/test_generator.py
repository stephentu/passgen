from passgen.generator import generate, generate_variable
from passgen.charsets import displayable_charset
from passgen.policies import one_letter_one_number

import itertools as it
import numpy as np

from nose.plugins.attrib import attr

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

@attr('slow')
def test_generator_fixed():
    charset = 'abcd'
    length = 3

    forward_map = list(''.join(x) for x in it.product(charset, repeat=length))
    reverse_map = { k : i for i, k in enumerate(forward_map) }

    nsamples, ntries = 10000, 100
    bins = np.zeros(len(forward_map), dtype=np.int)
    while ntries:
        for _ in xrange(nsamples):
            password = generate(charset, None, length=length, urandom=True)
            bins[reverse_map[password]] += 1
        hist = np.array(bins, dtype=np.float)
        hist /= hist.sum()
        freq = 1./float(len(forward_map))
        diff = np.abs(hist - freq)
        print ntries, diff.max(), freq/10.
        if diff.max() > freq/10.:
            ntries -= 1
            continue
        return # success
    assert False, "did not converge"

@attr('slow')
def test_generator_variable():
    charset = 'abcd'
    min_length, max_length = 2, 4

    len_range = xrange(min_length, max_length + 1)
    chain = it.chain.from_iterable(
        it.product(charset, repeat=l) for l in len_range)
    forward_map = list(''.join(x) for x in chain)
    reverse_map = { k : i for i, k in enumerate(forward_map) }

    nsamples, ntries = 10000, 100
    bins = np.zeros(len(forward_map), dtype=np.int)
    while ntries:
        for _ in xrange(nsamples):
            password = generate_variable(
                charset, None, min_length=min_length,
                max_length=max_length, urandom=True)
            bins[reverse_map[password]] += 1
        hist = np.array(bins, dtype=np.float)
        hist /= hist.sum()
        freq = 1./float(len(forward_map))
        diff = np.abs(hist - freq)
        print ntries, diff.max(), freq/10.
        if diff.max() > freq/10.:
            ntries -= 1
            continue
        return # success
    assert False, "did not converge"
