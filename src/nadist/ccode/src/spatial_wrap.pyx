# -*- coding: utf-8 -*-
#cython: boundscheck=False, wraparound=False, cdivision=True

"""
=======================
Cython Distance Wrapper
=======================

:Authors:
    Moritz E. Beber
:Date:
    2016-04-22
:Copyright:
    Copyright |c| 2016, Moritz E. Beber, all rights reserved.
:File:
    spatial_wrap.py

.. |c| unicode: U+A9
"""


import cython

from libc.stdint cimport uint8_t

import numpy as np
cimport numpy as np
np.import_array()


cdef extern from "spatial.c":
    inline double euclidean_distance(const double *u, const double *v,
        const uint8_t *u_mask, const uint8_t *v_mask, const Py_ssize_t num)

def euclidean_pdist(np.ndarray[np.double_t, ndim=2, mode="c"] arr,
        np.ndarray[np.uint8_t, ndim=2, cast=True, mode="c"] mask):
    cdef Py_ssize_t num_vec = arr.shape[0]
    cdef Py_ssize_t num_dim = arr.shape[1]
    cdef Py_ssize_t i = 0
    cdef Py_ssize_t j = 0
    cdef Py_ssize_t k = 0
    cdef np.ndarray[np.double_t, ndim=1, mode="c"] dists = np.zeros(num_vec * (num_vec - 1) // 2,
            dtype=np.double)
    for i in range(num_vec - 1):
        for j in range(i + 1, num_vec):
            dists[k] = euclidean_distance(&arr[i, 0], &arr[j, 0], <uint8_t*>&mask[i, 0],
                    <uint8_t*>&mask[j, 0], num_dim)
            k += 1
    return dists
