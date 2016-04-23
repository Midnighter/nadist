/* ================
 * Distance
 * ================
 *
 * :Authors:
 *     Moritz E. Beber
 * :Date:
 *     2016-04-22
 * :Copyright:
 *     Copyright |c| 2016, Moritz E. Beber, all rights reserved.
 * :File:
 *     spatial.c
 */



//#include <numpy/ndarrayobject.h>

#include <stdlib.h>
#include <math.h>
#include <Python.h>


inline double
euclidean_distance(const double *u, const double *v, const uint8_t *u_mask,
        const uint8_t *v_mask, const Py_ssize_t num)
{
    Py_ssize_t i = 0;
    Py_ssize_t miss = 0;
    double total = 0.0;
    double diff = 0.0;
    for (i = 0; i < num; ++i) {
        if (u_mask[i] || v_mask[i]) {
            ++miss;
        }
        else {
            diff = u[i] - v[i];
            total += diff * diff;
        }
    }
    if (miss == num) {
        return NAN;
    }
    // distance correction for missing values
    return (double)(num) / (double)(num - miss) * sqrt(total);
}
