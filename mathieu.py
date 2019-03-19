"""
Module implements algorithm presented by Vernizzi: http://www.fis.unipr.it/~coisson/Mathieu.pdf to obtain the
characteristic values of Mathieu equation: y" + (a + 2q cos(2x))y = 0.
"""

import numpy as np


def characteristic_a(q: float, ndim: int = 101):
    """
    Function computes the characteristic 'a' values of the Mathieu equation. These are generally called a_n and b_n in
    an ordered manner depending on whether q is positive or negative (see reference above).
    :param q: the q parameter of the Mathieu equation. float or complex
    :param ndim: the size of the matrix used in the computation. Mathematically the result is correct only for ndim->inf
                thus higher values will yield more accurate results at the expense of computation time
    :return: the unsorted numpy array of characteristic values.
    """
    # setup the matrix
    h_mat = [[0.0]*ndim for _ in range(ndim)]

    for i in range(ndim):
        for j in range(ndim):
            if j == i-2 or j == i+2:
                h_mat[i][j] = q
            if j == i:
                h_mat[i][j] = int(i-ndim//2)**2

    h_mat = np.array(h_mat)
    return np.linalg.eigvals(h_mat)
