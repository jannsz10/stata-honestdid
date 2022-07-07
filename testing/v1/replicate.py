from scipy.optimize import minimize
import numpy as np


sigma = np.array([
    [ 8.428358e-04,  4.768687e-04, 2.618051e-04, 0.0002354220, 0.0001676371, 0.0001128708, 1.992816e-05, -1.368265e-04],
    [ 4.768687e-04,  6.425420e-04, 3.987425e-04, 0.0002435515, 0.0002201960, 0.0001804591, 3.843765e-05, -2.960422e-05],
    [ 2.618051e-04,  3.987425e-04, 5.229950e-04, 0.0002117686, 0.0001840722, 0.0001458528, 7.005197e-05,  5.952995e-05],
    [ 2.354220e-04,  2.435515e-04, 2.117686e-04, 0.0003089595, 0.0001197866, 0.0001334081, 1.016335e-04,  1.079052e-04],
    [ 1.676371e-04,  2.201960e-04, 1.840722e-04, 0.0001197866, 0.0003599704, 0.0002478819, 1.749579e-04,  1.654257e-04],
    [ 1.128708e-04,  1.804591e-04, 1.458528e-04, 0.0001334081, 0.0002478819, 0.0004263950, 2.171438e-04,  2.892748e-04],
    [ 1.992816e-05,  3.843765e-05, 7.005197e-05, 0.0001016335, 0.0001749579, 0.0002171438, 4.886698e-04,  3.805322e-04],
    [-1.368265e-04, -2.960422e-05, 5.952995e-05, 0.0001079052, 0.0001654257, 0.0002892748, 3.805322e-04,  7.617394e-04]
])

A_quadratic_sd = np.array([
    [0, 0, 0, 0,             0,             0,             0,             0],
    [0, 0, 0, 0,             0,             0,             0,             0],
    [0, 0, 0, 0,             0,             0,             0,             0],
    [0, 0, 0, 0,             0,             0,             0,             0],
    [0, 0, 0, 0,   .0005316404,  -.0000287359,  -.0001288079,  -8.12950e-06],
    [0, 0, 0, 0,  -.0000287359,    .000368052,  -.0001560354,   .0000317829],
    [0, 0, 0, 0,  -.0001288079,  -.0001560354,   .0004084173,  -.0000971909],
    [0, 0, 0, 0,  -8.12950e-06,   .0000317829,  -.0000971909,   .0003089595]
])

A_lienar_sd = np.array([
     0.000000e+00,
     0.000000e+00,
     0.000000e+00,
     0.000000e+00,
    -1.051178e-04,
     7.224761e-05,
     1.285712e-04,
     2.395732e-04
])

A_constant_sd = 0.0003599704