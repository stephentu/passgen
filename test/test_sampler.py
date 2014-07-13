from passgen.sampler import sample

import numpy as np

def _assert_uniform_dist0(n, f, nsamples, history, ntries):
    assert nsamples > 0
    history.extend([sample(n, f) for _ in xrange(nsamples)])
    samples = np.array(history, dtype=int)
    hist = np.array(np.bincount(samples, minlength=n), dtype=np.float)
    hist /= hist.sum()
    freq = 1./float(n)
    diffs = np.abs(hist - freq)
    if diffs.max() > 0.01:
        if ntries:
            _assert_uniform_dist0(n, f, nsamples, history, ntries - 1)
        else:
            assert False, 'probabilities did not converge to uniform'

def _assert_uniform_dist(n, f, nsamples, ntries=3):
    assert ntries > 0
    _assert_uniform_dist0(n, f, nsamples, [], ntries)

def test_histograms_LT_256():
    with open('/dev/urandom') as f:
        _assert_uniform_dist(5, f, nsamples=10000)
        _assert_uniform_dist(13, f, nsamples=10000)
        _assert_uniform_dist(2, f, nsamples=10000)
        _assert_uniform_dist(184, f, nsamples=10000)
        _assert_uniform_dist(255, f, nsamples=10000)

def test_histograms_GE_256():
    with open('/dev/urandom') as f:
        _assert_uniform_dist(256, f, nsamples=10000)
        _assert_uniform_dist(4327, f, nsamples=10000)
        _assert_uniform_dist(10000, f, nsamples=10000)
