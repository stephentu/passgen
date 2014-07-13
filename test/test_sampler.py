from passgen.sampler import sample, sample_uniform_01, \
        sample_discrete_log, str2int

import numpy as np

from nose.plugins.attrib import attr

def _assert_uniform_dist0(n, f, nsamples, history, ntries):
    assert nsamples > 0
    history.extend([sample(n, f) for _ in xrange(nsamples)])
    samples = np.array(history, dtype=int)
    hist = np.array(np.bincount(samples, minlength=n), dtype=np.float)
    hist /= hist.sum()
    freq = 1./float(n)
    diffs = np.abs(hist - freq)
    if diffs.max() > 0.005:
        if ntries:
            _assert_uniform_dist0(n, f, nsamples, history, ntries - 1)
        else:
            print n, hist
            assert False, 'probabilities did not converge to uniform'
    # passed
    print n, hist

def _assert_uniform_dist(n, f, nsamples, ntries=3):
    assert ntries > 0
    _assert_uniform_dist0(n, f, nsamples, [], ntries)

def test_histograms_LT_256():
    with open('/dev/urandom') as f:
        for i in xrange(2, 20):
            _assert_uniform_dist(i, f, nsamples=50000)
        _assert_uniform_dist(184, f, nsamples=10000)
        _assert_uniform_dist(255, f, nsamples=10000)

def test_histograms_GE_256():
    with open('/dev/urandom') as f:
        _assert_uniform_dist(256, f, nsamples=10000)
        _assert_uniform_dist(4327, f, nsamples=10000)
        _assert_uniform_dist(10000, f, nsamples=10000)

def test_str2int():
    x = 8522348329432189L
    y = x
    s = ''
    while y:
        s += chr(y & 0xFF)
        y >>= 8
    assert str2int(s) == x

def test_sample_uniform_01():
    nsamples, nbins, ntries = 100000, 100, 3
    with open('/dev/urandom') as f:
        samples = []
        while ntries:
            samples.extend([sample_uniform_01(f) for _ in xrange(nsamples)])
            hist = np.array(
                np.histogram(samples, bins=nbins, range=(0.0, 1.0), density=False)[0],
                dtype=np.float)
            hist /= hist.sum()
            freq = 1./float(nbins)
            diffs = np.abs(hist - freq)
            if diffs.max() > (freq/10.):
                ntries -= 1
                continue
            return # success
        assert False, 'did not converge'

def test_sample_discrete_log():
    probs = np.array([0.3, 0.1, 0.6])
    scores = np.log(probs)
    counts = np.zeros(len(probs), dtype=np.int)
    nsamples, ntries = 10000, 3
    with open('/dev/urandom') as f:
        while ntries:
            for _ in xrange(nsamples):
                counts[sample_discrete_log(scores, f)] += 1
            dist = np.array(counts, dtype=np.float)
            dist /= dist.sum()
            if np.linalg.norm(probs - dist) > 0.01:
                ntries -= 1
                continue
            return # success
        assert False, 'did not converge'
