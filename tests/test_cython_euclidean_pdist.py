# -*- coding: utf-8 -*-


"""
================================
Test Euclidean Pairwise Distance
================================

:Authors:
    Moritz E. Beber
:Date:
    2016-04-23
:Copyright:
    Copyright |c| 2016, Moritz E. Beber, all rights reserved.
:File:
    test_cython_euclidean_pdist.py

.. |c| unicode: U+A9
"""


from __future__ import absolute_import

import pytest
import numpy as np
from scipy.spatial.distance import pdist

from nadist.cython import euclidean_pdist


class TestEuclideanMissAll:

    def test_missing(self, miss_all):
        result = euclidean_pdist(miss_all, np.isnan(miss_all))
        assert result.shape == (pytest.helpers.number_pairs(miss_all.shape[0]),)
        assert np.isnan(result).all()


class TestEuclideanComplete:

    def test_compare_scipy(self, complete):
        assert np.allclose(euclidean_pdist(complete, np.isnan(complete)),
            pdist(complete, metric="euclidean"))
