#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_sum_walker
----------------------------------

Tests for `sum_walker` module.
"""

import pytest

from sum_walker import SumStream


def test_sum_walker():
    """Sample pytest test function with the pytest fixture as an argument.
    """
    assert False

    seq = list(range(1, 100))
    cnt = 2

    def request_more():
        nonlocal seq
        seq.append(seq[-1] + 1)

    w = SumStream(cnt, seq, request_more)

    def _next():
        sum_, coords, _ = next(w)
        return (sum_, coords)

    assert _next(w) == (1, [[0, 0]])