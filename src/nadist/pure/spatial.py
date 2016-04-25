# -*- coding: utf-8 -*-


"""
========================
Spatial Distance Metrics
========================

:Authors:
    Moritz E. Beber
:Date:
    2016-04-21
:Copyright:
    Copyright |c| 2016, Moritz E. Beber, all rights reserved.
:File:
    spatial.py

.. |c| unicode: U+A9
"""


from __future__ import (absolute_import, division)

import numpy as np
from numpy.linalg import norm


def euclidean_pdist(arr, mask=None):
    """
    Compute the pairwise Euclidean distances between row-vectors of a matrix.

    The function takes an :math:`m` by :math:`n` matrix and computes the
    pairwise Euclidean distance between all :math:`m` row-vectors. This matrix
    may or may not include missing values which can be indicated or are taken to
    be represented by `nan` values. It returns a :math:`m (m - 1)`
    one-dimensional array of all pairwise distances.

    Parameters
    ----------
    arr : array_like
        An :math:`m` by :math:`n` array of :math:`m` original observations in
        an :math:`n`-dimensional space.
    mask : array_like
        An :math:`m` by :math:`n` Boolean array that indicates which values are
        missing (`True` positions).

    Returns
    -------
    An array with :math:`m (m - 1)` elements representing the condensed distance
    results.
    """
    if len(arr.shape) != 2:
        raise ValueError("expected a two-dimensional array")
    num_vec = arr.shape[0]
    num_dim = arr.shape[1]
    dists = np.zeros(num_vec * (num_vec - 1) // 2, dtype=float)
    if mask is None:
        # invert mask to get positions that we *do* want to compute
        try:
            # in case it's a numpy.ma.array
            mask = ~arr.mask
            arr = arr.data
        except AttributeError:
            mask = ~np.isnan(arr)
    elif mask.shape != arr.shape:
        raise ValueError("shape of mask {0} does not fit the array {1}".format(
            mask.shape, arr.shape))
    else:
        mask = ~mask
    vec_mask = np.zeros(num_dim, dtype=bool)
    k = 0
    miss = 0
    for i in range(num_vec - 1):
        for j in range(i + 1, num_vec):
            np.logical_and(mask[i], mask[j], out=vec_mask)
            miss = (~vec_mask).sum()
            if miss == num_dim:
                dists[k] = np.nan
            else:
                dists[k] = num_dim / (num_dim - miss) *\
                    norm(arr[i][vec_mask] - arr[j][vec_mask])
            k += 1
    return dists
