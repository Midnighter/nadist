# -*- coding: utf-8 -*-


"""
========================
Directory-Level Fixtures
========================

:Authors:
    Moritz E. Beber
:Date:
    2016-04-23
:Copyright:
    Copyright |c| 2016, Moritz E. Beber, all rights reserved.
:File:
    conftest.py

.. |c| unicode: U+A9
"""


from __future__ import absolute_import

pytest_plugins = ["helpers_namespace"]

import pytest
import numpy as np


@pytest.fixture(scope="session",
    params=[1, 3, 4, 5],
    ids=["{0:d}D".format(x) for x in [1, 3, 4, 5]])
def dimension(request):
    return np.zeros(shape=(10,) * request.param, dtype=float)

@pytest.fixture(scope="session")
def miss_all():
    miss = np.empty((10, 100), dtype=float)
    miss.fill(np.nan)
    return miss

@pytest.fixture(scope="session",
    params=[(33, 303), (303, 3003),
    pytest.mark.skipif(True, reason="too slow")(3003, 300003)],
    ids=["small", "medium", "large"])
def complete(request):
    np.random.seed(1234567890)
    return np.random.rand(*request.param)

@pytest.fixture(scope="session",
    params=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
def partial_mask(request, complete):
    return (complete < request.param)

@pytest.helpers.register
def number_pairs(dim):
    return dim * (dim - 1) // 2
