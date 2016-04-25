# -*- coding: utf-8 -*-
#cython: boundscheck=False, wraparound=False, cdivision=True


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
    spatial.pyx

.. |c| unicode: U+A9
"""


from __future__ import absolute_import

import cython
from libc.math cimport (pow, sqrt)

import numpy as np
cimport numpy as np
np.import_array()


def euclidean_pdist(np.ndarray[np.double_t, ndim=2, mode="c"] arr,
        np.ndarray[np.uint8_t, ndim=2, cast=True, mode="c"] mask):
    if arr.shape[0] != mask.shape[0] or arr.shape[1] != mask.shape[1]:
        raise ValueError("shape of mask ({0:d}, {1:d}) does not fit the array "\
            "({2:d}, {3:d})".format(mask.shape[0], mask.shape[1], arr.shape[0],
            arr.shape[1]))
    cdef Py_ssize_t num_vec = arr.shape[0]
    cdef Py_ssize_t num_dim = arr.shape[1]
    cdef Py_ssize_t i = 0
    cdef Py_ssize_t j = 0
    cdef Py_ssize_t k = 0
    cdef Py_ssize_t z = 0
    cdef Py_ssize_t miss = 0
    cdef np.ndarray[np.double_t, ndim=1] dists = np.zeros(num_vec * (num_vec - 1) // 2,
            dtype=np.double)
    for i in range(num_vec - 1):
        for j in range(i + 1, num_vec):
            miss = 0
            for k in range(num_dim):
                if mask[i, k] or mask[j, k]:
                    miss += 1
                    continue
                dists[z] += pow(arr[i, k] - arr[j, k], 2.0)
            if miss == num_dim:
                dists[z] = np.nan
            else:
                dists[z] = <double>(num_dim) / <double>(num_dim - miss) * sqrt(dists[z])
            z += 1
    return dists
