"""
Helium-e momentum transfer cross section values from:
Pack, J.L. et al. in J. Appl. Phys. 71, 5363, 1992.

Transcribed by Ben Yee
"""

from constants import q
from numpy import array
from scipy.interpolate import UnivariateSpline

E = array([0.000, 0.0025, 0.0036, 0.010, 0.032, 0.200, 0.600, 1.400, 3.000,
           8.000, 14.000, 18.00,  20.00, 25.00, 35.00, 40.00, 50.00, 75.00,
           100.0, 150.0,  200.0,  250.0, 300.0, 500.0, 700.0]) * q

Q = array([4.95, 5.00, 5.10, 5.27, 5.52, 6.20, 6.66, 6.98, 6.93, 5.50, 3.60,
           2.90, 2.69, 2.00, 1.26, 1.00, 0.70, 0.36, 0.22, 0.12, 0.07, 0.05,
           0.036, 0.016, 0.009]) * 1e-20

def sigma(x):
    s = UnivariateSpline(E, Q, s=0, k=3)
    return s(x)
