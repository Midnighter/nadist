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
    test_euclidean_pdist.py

.. |c| unicode: U+A9
"""


from __future__ import absolute_import

import pytest
import numpy as np
from scipy.spatial.distance import pdist

from nadist.pure import euclidean_pdist


class TestShapes:

    def test_wrong_shape(self, dimension):
        with pytest.raises(ValueError):
            euclidean_pdist(dimension)

    def test_mask_shape(self, complete):
        with pytest.raises(ValueError):
            euclidean_pdist(complete, np.isnan(complete[:complete.shape[0] - 10,
                :complete.shape[1] - 10]))


class TestEuclideanMissAll:

    def test_missing_default_mask(self, miss_all):
        result = euclidean_pdist(miss_all)
        assert result.shape == (pytest.helpers.number_pairs(miss_all.shape[0]),)
        assert np.isnan(result).all()

    def test_missing_masked_array(self, miss_all):
        m_arr = np.ma.masked_where(np.isnan(miss_all), miss_all)
        result = euclidean_pdist(m_arr)
        assert result.shape == (pytest.helpers.number_pairs(miss_all.shape[0]),)
        assert np.isnan(result).all()

    def test_missing_mask(self, miss_all):
        result = euclidean_pdist(miss_all, np.isnan(miss_all))
        assert result.shape == (pytest.helpers.number_pairs(miss_all.shape[0]),)
        assert np.isnan(result).all()


class TestEuclideanComplete:

    def test_compare_scipy(self, complete):
        assert np.allclose(euclidean_pdist(complete),
            pdist(complete, metric="euclidean"))
