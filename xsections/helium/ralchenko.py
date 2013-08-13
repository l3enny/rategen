"""
Electron-Atom Excitation Cross Section Constants for Helium
author: Ben Yee
last revised: 2012-05-08

This file contains the fitting constants necessary to generate the
cross section data for helium. 

Yu. Ralchenko et al. Atomic Data and Nuclear Data Tables 94 (2008)
603-622.
"""

from states import states
from constants import *
import numpy as np
from numpy import log

# transition list format:
# constants = {
#    InitialState1:{FinalState1:{'type':'da|df|sf', 'A':(fitting constants)},
#                   FinalState2:{'type':'da|df|sf', 'A':(fitting constants)}},
#    InitialState2:{FinalState1:{'type':'da|df|sf', 'A':(fitting constants)},
#                   FinalState2:{'type':'da|df|sf', 'A':(fitting constants)}},
#    etc ...
#             }
constants = {
    100:{201:{'type':'da',
              'A':(+7.087e-1, -9.347e-2, -1.598e+0,
                   +2.986e+0, -1.293e+0, +3.086e-1)},
         301:{'type':'da',
              'A':(+1.730e-1, +2.410e-2, -4.709e-1,
                   +7.690e-1, -3.216e-1, +8.568e-1)},
         401:{'type':'da',
              'A':(+6.923e-2, +6.893e-3, -2.079e-1,
                   +3.508e-1, -1.497e-1, +4.280e-2)},
         200:{'type':'df',
              'A':(+1.888e-1, -5.754e-1, +3.439e+0, -2.088e+0, +2.544e+1)},
         300:{'type':'df',
              'A':(+4.033e-2, -1.872e-2, +2.368e+0, -1.379e+0, +1.258e+2)},
         302:{'type':'df',
              'A':(+9.708e-3, +2.855e-2, -8.265e-2, +4.944e-2, +1.992e-1)},
         400:{'type':'df',
              'A':(+1.613e-2, -5.564e-2, +2.943e-1, -2.024e-1, +2.342e+1)},
         402:{'type':'df',
              'A':(+5.420e-3, +1.198e-2, -3.173e-2, +1.606e-2, +1.060e-1)},
         403:{'type':'df',
              'A':(+4.383e-5, -1.033e-4, +3.772e-3, +1.631e-2, +5.644e+1)},
         211:{'type':'sf',
              'A':(+2.823e-1, +2.048e+0, +5.287e+0, -7.363e+0, +2.728e+1)},
         210:{'type':'sf',
              'A':(+6.888e-1, +1.975e-1, +7.232e+0, -4.839e+0, +5.003e+1)},
         312:{'type':'sf',
              'A':(+2.207e-3, +8.429e-3, +1.816e-1, -1.812e-1, +9.544e+0)},
         311:{'type':'sf',
              'A':(+6.730e-2, +5.465e-1, -4.434e-1, -1.042e-1, +1.140e+1)},
         310:{'type':'sf',
              'A':(+9.392e-2, -1.641e-1, +7.605e-2, -4.536e-3, -9.246e-1)},
         412:{'type':'sf',
              'A':(+1.334e-3, +1.819e-2, -3.848e-2, +1.896e-2, -9.893e-1)},
         413:{'type':'sf',
              'A':(+0.000e+0, +4.079e-4, -3.863e-4, +1.701e-5, -9.497e-1)},
         411:{'type':'sf',
              'A':(+2.585e-2, +2.275e-1, -5.827e-2, -1.615e-1, +1.505e+1)},
         410:{'type':'sf',
              'A':(+3.008e-2, -3.956e-2, -1.940e-3, +1.154e-2, -9.813e-1)},
         'ion':{'type':'ion',
              'A':(+5.857e-1, -4.457e-1, +7.680e-1,
                   -2.521e+0, +3.317e+0, +0.000e+0)}},

    200:{201:{'type':'da',
              'A':(+3.404e+1, +7.267e+1, +1.710e+2,
                   -7.033e+2, +4.704e+2, +1.194e+1)},
         301:{'type':'da',
              'A':(+3.3360+0, -1.147e+0, -4.889e+0,
                   +2.023e+1, -1.336e+1, +1.059e+1)},
         401:{'type':'da',
              'A':(+8.826e-1, -3.618e-1, -1.231e+0,
                   +5.606e+0, -3.985e+0, +5.890e+0)},
         300:{'type':'df',
              'A':(+3.762e+0, -1.140e+1, +1.403e+1, -5.377e+0, +1.010e+0)},
         302:{'type':'df',
              'A':(+1.058e+1, +3.485e+1, +7.830e+1, -1.043e+2, +5.370e+1)},
         400:{'type':'df',
              'A':(+7.829e-1, -2.417e+0, +2.876e+0, -1.108e+0, +0.000e+0)},
         402:{'type':'df',
              'A':(+1.872e+0, +5.458e+0, -6.857e+0, +5.902e+0, +3.358e+1)},
         403:{'type':'df',
              'A':(+5.041e-1, +4.182e+0, -6.329e+0, +3.139e+0, +9.425e+0)},
         211:{'type':'sf',
              'A':(+5.983e+2, -5.310e+2, +3.348e+2, -2.412e+2, +2.239e+2)},
         312:{'type':'sf',
              'A':(+4.042e+0, +1.358e+2, +8.142e+1, -2.085e+2, +1.737e+2)},
         311:{'type':'sf',
              'A':(+1.382e+0, +8.314e+1, +2.834e+2, -1.831e+2, +3.176e+2)},
         310:{'type':'sf',
              'A':(+6.648e-1, +1.940e+3, +6.935e+2, +1.447e+3, +6.339e+3)},
         412:{'type':'sf',
              'A':(+9.480e-1, +2.121e+1, -7.385e+0, -1.085e+1, +7.917e+1)},
         413:{'type':'sf',
              'A':(+2.338e-1, -6.755e+1, +8.613e+3, -8.035e+3, +1.772e+4)},
         411:{'type':'sf',
              'A':(+2.701e-1, +1.187e+1, +7.598e+0, +1.182e+0, +1.051e+2)},
         410:{'type':'sf',
              'A':(+1.236e-1, +2.041e+2, -2.538e+2, +1.090e+3, +3.582e+3)},
         'ion':{'type':'ion',
              'A':(+3.076e-1, -2.748e-1, +4.462e-1,
                   -1.841e-1, +1.336e+0, -1.775e+0)}},

    201:{300:{'type':'da',
              'A':(+4.604e+0, -2.204e+0, -1.093e+1,
                   +3.893e+1, -2.440e+1, +5.612e+0)},
         302:{'type':'da',
              'A':(+6.255e+1, +4.458e+1, -2.409e+2,
                   +4.069e+2, -1.955e+2, +1.055e+1)},
         400:{'type':'da',
              'A':(+5.545e-1, -4.400e-4, -6.360e-1,
                   +1.785e+0, -4.656e-1, +3.675e+0)},
         402:{'type':'da',
              'A':(+7.910e+0, +9.449e+0, -4.534e+1,
                   +7.295e+1, -3.374e+1, +5.963e+0)},
         301:{'type':'df',
              'A':(+1.689e+1, -4.916e+1, +1.185e+2, -7.711e+1, +1.079e+1)},
         403:{'type':'df',
              'A':(+4.731e+0, +2.708e+1, -3.209e+1, +1.993e+1, +2.372e+1)},
         401:{'type':'df',
              'A':(+3.599e+0, -1.267e+1, +1.916e+1, -1.007e+1, +0.000e+0)},
         312:{'type':'sf',
              'A':(+1.702e+1, +1.484e+3, -4.593e+2, -8.789e+2, +3.229e+2)},
         322:{'type':'sf',
              'A':(+1.093e+1, +8.331e+3, +1.929e+4, -1.731e+4, +5.540e+3)},
         320:{'type':'sf',
              'A':(+4.980e+0, +4.415e+2, +1.002e+3, -8.063e+2, +5.626e+2)},
         412:{'type':'sf',
              'A':(+3.686e+0, +1.887e+2, -9.472e+0, -1.471e+2, +1.729e+2)},
         413:{'type':'sf',
              'A':(+8.678e-1, +3.062e+1, -3.479e+1, +1.127e+1, +3.760e+1)},
         411:{'type':'sf',
              'A':(+2.243e+0, +5.624e+2, +8.402e+2, -3.634e+2, +1.504e+3)},
         410:{'type':'sf',
              'A':(+6.494e-1, +2.526e+1, -1.162e+0, +5.160e+1, +1.225e+2)},
         'ion':{'type':'ion',
              'A':(+2.068e-1, -2.034e-1, +5.759e-1,
                   -2.442e-1, +1.986e+0, -2.019e+0)}},

    300:{301:{'type':'da',
              'A':(+1.837e+2, +5.147e+2, -2.760e+3,
                   +4.081e+3, -1.832e+3, +2.332e+1)},
         401:{'type':'da',
              'A':(+1.517e+1, -3.469e+1, +7.918e+1,
                   -6.474e+1, +2.026e+1, +2.138e+0)},
         302:{'type':'df',
              'A':(+4.273e+1, -1.488e+1, -1.041e+2, +7.962e+1, +1.700e+0)},
         400:{'type':'df',
              'A':(+1.523e+1, -8.159e+1, +1.695e+2, -9.929e+1, +5.103e+0)},
         402:{'type':'df',
              'A':(+2.585e+1, -8.587e+1, +1.017e+2, -4.008e+1, +0.000e+0)},
         403:{'type':'df',
              'A':(+1.939e+1, -4.539e+1, +3.911e+1, -1.204e+1, +0.000e+0)},
         312:{'type':'sf',
              'A':(+6.729e+2, +6.022e+5, -2.032e+6, +1.788e+6, +2.709e+4)},
         311:{'type':'sf',
              'A':(+1.242e+3, +1.094e+7, -2.101e+7, +1.138e+7, +3.429e+5)},
         412:{'type':'sf',
              'A':(+4.674e+0, +2.273e+2, +7.469e+2, -8.390e+2, +2.907e+2)},
         413:{'type':'sf',
              'A':(+1.601e+0, +1.311e+3, +5.193e+2, -1.588e+3, +4.897e+2)},
         411:{'type':'sf',
              'A':(+1.878e+0, +7.168e+2, +1.402e+3, +6.210e+1, +1.290e+3)},
         410:{'type':'sf',
              'A':(+1.395e+0, +1.370e+4, -3.392e+4, +7.064e+4, +2.137e+4)},
         'ion':{'type':'ion',
              'A':(+1.787e-1, -1.775e-1, +7.023e-1,
                   -1.132e+0, +3.727e+0, -3.255e+0)}},

    302:{301:{'type':'da',
              'A':(+2.932e+2, +8.061e+2, +1.229e+5,
                   -9.222e+5, +1.898e+6, +1.134e+2)},
         403:{'type':'da',
              'A':(+4.145e+2, +3.149e+2, -2.065e+3,
                   +3.516e+3, -1.650e+3, +2.407e+1)},
         401:{'type':'da',
              'A':(+3.712e+0, +2.713e+0, -5.615e+0,
                   +5.290e+0, -2.158e+0, +0.000e+0)},
         400:{'type':'df',
              'A':(+5.089e+0, -2.327e+1, +5.943e+1, -4.074e+1, +6.132e-1)},
         402:{'type':'df',
              'A':(+9.109e+1, -2.982e+2, +6.165e+2, -3.155e+2, +1.178e+1)},
         412:{'type':'sf',
              'A':(+4.743e+1, +1.223e+5, +2.074e+5, -2.893e+5, +1.904e+4)},
         413:{'type':'sf',
              'A':(+6.314e+1, +2.583e+4, -5.741e+3, -1.452e+4, +1.536e+3)},
         411:{'type':'sf',
              'A':(+0.000e+0, +3.369e+3, +6.115e+3, -5.152e+3, +8.638e+2)},
         410:{'type':'sf',
              'A':(+1.499e+0, +1.809e+3, +1.005e+3, -6.550e+2, +9.339e+2)},
         'ion':{'type':'ion',
              'A':(+9.637e-2, -9.370e-2, +1.051e+0,
                   -4.831e+0, +1.251e+1, -8.287e+0)}},

    301:{400:{'type':'da',
              'A':(+7.884e+0, +1.097e+2, -5.543e+2,
                   +1.008e+3, -5.630e+2, +3.559e+1)},
         402:{'type':'da',
              'A':(+1.629e+2, +6.048e+1, -1.055e+3,
                   +2.398e+3, -1.390e+3, +2.594e+1)},
         403:{'type':'df',
              'A':(+1.542e+2, +7.434e+2, +4.114e+2, -5.986e+2, +2.059e+2)},
         401:{'type':'df',
              'A':(+6.444e+1, -2.365e+2, +4.775e+2, -3.084e+2, +1.641e+1)},
         412:{'type':'sf',
              'A':(+1.470e+1, +5.349e+3, +5.281e+3, -9.207e+3, +1.556e+3)},
         413:{'type':'sf',
              'A':(+7.766e+1, +1.248e+4, +8.902e+3, -2.051e+4, +2.003e+3)},
         411:{'type':'sf',
              'A':(+1.125e+1, +1.295e+5, +5.808e+4, -8.942e+4, +4.622e+4)},
         410:{'type':'sf',
              'A':(+7.973e+0, +5.673e+3, +5.417e+3, -6.546e+3, +3.901e+3)},
         'ion':{'type':'ion',
              'A':(+1.654e-1, -1.640e-1, +3.123e-1,
                   -4.326e-2, +1.729e+0, -1.691e+0)}},

    400:{401:{'type':'da',
              'A':(+6.787e+2, +9.856e+2, -1.751e+4,
                   -4.424e+3, +2.284e+5, +1.876e+1)},
         403:{'type':'df',
              'A':(+1.681e+2, -7.059e+2, +1.022e+3, -4.831e+2, +0.000e+0)},
         402:{'type':'df',
              'A':(+3.016e+1, -8.980e+2, +2.240e+4, -2.150e+4, +2.749e+2)},
         412:{'type':'sf',
              'A':(+9.651e+2, +3.404e+7, -1.015e+8, +7.969e+7, +1.764e+6)},
         413:{'type':'sf',
              'A':(+2.102e+2, +8.995e+5, -2.902e+6, +2.495e+6, +3.244e+4)},
         411:{'type':'sf',
              'A':(+2.968e+3, +1.709e+8, -4.113e+8, +3.782e+8, +4.486e+6)},
         'ion':{'type':'ion',
              'A':(+1.206e-1, -1.136e-1, +7.407e-1,
                   -3.115e+0, +7.325e+0, -4.900e+0)}},

    402:{403:{'type':'da',
              'A':(+1.498e+3, +3.296e+3, +1.250e+4,
                   -2.970e+4, +1.501e+4, +6.435e+0)},
         401:{'type':'da',
              'A':(+1.161e+3, +3.649e+3, +6.912e+5,
                   -1.081e+7, +5.967e+7, +1.523e+2)},
         413:{'type':'sf',
              'A':(+8.165e+7, -4.651e+8, +9.297e+8, -5.415e+8, +7.004e+6)},
         'ion':{'type':'ion',
              'A':(+1.814e-2, +1.047e-2, +6.380e-2,
                   +1.172e+0, -9.804e-1, +3.382e-1)}},
    
    403:{401:{'type':'df',
              'A':(+1.655e+2, +3.062e+3, +2.503e+4, -2.822e+4, +2.256e+2)},
         'ion':{'type':'ion',
              'A':(+4.340e-2, +1.216e-2, +3.506e-1,
                   -1.911e+0, +6.694e+0, -4.631e+0)}},

    210:{211:{'type':'da',
              'A':(+7.696e+1, +1.250e+2, +4.938e+1,
                   -4.778e+2, +3.189e+2, +8.157e+0)},
         311:{'type':'da',
              'A':(+3.292e+0, -3.594e+0, +3.934e+0,
                   +1.138e+1, -8.145e+0, +3.360e+0)},
         411:{'type':'da',
              'A':(+9.700e-1, -4.920e-1, +1.629e+0,
                   +5.632e-1, +4.405e-2, +5.963e+0)},
         310:{'type':'df',
              'A':(+8.344e+0, -2.658e+1, +3.488e+1, -1.431e+1, +0.000e+0)},
         312:{'type':'df',
              'A':(+1.679e+1, +5.841e+1, +3.435e+2, -3.922e+2, +6.290e+1)},
         410:{'type':'df',
              'A':(+1.636e+0, -3.577e+0, +1.959e+0, +8.521e-1, +0.000e+0)},
         412:{'type':'df',
              'A':(+4.063e+0, +1.541e+1, +6.089e+1, -7.115e+1, +5.762e+1)},
         413:{'type':'df',
              'A':(+5.676e-1, +4.383e+0, +9.326e+0, -9.539e+0, +1.816e+1)},
         201:{'type':'sf',
              'A':(+4.893e+1, +4.251e+3, -4.330e+3, +1.934e+2, +8.928e+2)},
         200:{'type':'sf',
              'A':(+5.475e+1, +3.483e+5, +2.345e+5, -5.090e+5, +5.424e+4)},
         302:{'type':'sf',
              'A':(+1.854e+0, +3.979e+1, +4.699e+0, -2.647e+1, +8.091e+1)},
         301:{'type':'sf',
              'A':(+1.383e+0, +5.353e+1, +3.937e+2, -4.378e+2, +4.331e+2)},
         300:{'type':'sf',
              'A':(+6.561e-1, +5.721e+2, +2.975e+3, -1.773e+3, +5.210e+3)},
         402:{'type':'sf',
              'A':(+5.492e-1, +8.462e+0, -1.079e+1, +5.007e+0, +3.464e+1)},
         403:{'type':'sf',
              'A':(+8.208e-2, -1.311e+1, +1.155e+3, -1.001e+3, +5.398e+3)},
         401:{'type':'sf',
              'A':(+3.412e-1, +9.770e+0, +2.173e+2, -2.240e+2, +5.031e+2)},
         400:{'type':'sf',
              'A':(+1.694e-1, +7.331e+1, +8.903e+1, +1.828e+2, +2.183e+3)},
         'ion':{'type':'ion',
              'A':(+2.427e-1, -1.900e-1, +3.205e-1,
                   +7.631e-1, -8.329e-1, -2.405e-1)}},

    211:{310:{'type':'da',
              'A':(+1.929e+1, +4.277e+0, -6.306e+1,
                   +1.483e+2, -6.056e+1, +8.088e+0)},
         312:{'type':'da',
              'A':(+1.414e+2, +9.031e+1, -6.238e+2,
                   +1.183e+3, -6.424e+2, +8.626e+0)},
         410:{'type':'da',
              'A':(+2.198e+0, +2.445e-1, -4.386e-1,
                   -1.691e+0, +7.824e+0, +4.614e+0)},
         412:{'type':'da',
              'A':(+2.209e+1, +2.204e+1, -1.161e+2,
                   +2.050e+2, -1.064e+2, +5.876e+0)},
         311:{'type':'df',
              'A':(+4.512e+1, -1.261e+2, +2.152e+2, -6.746e+1, +4.133e+0)},
         411:{'type':'df',
              'A':(+9.110e+0, -2.180e+1, +2.242e+1, -5.746e+0, +0.000e+0)},
         413:{'type':'df',
              'A':(+9.560e+0, +5.997e+1, +3.657e+1, -5.017e+1, +3.155e+1)},
         201:{'type':'sf',
              'A':(+7.477e+3, -7.356e+1, -1.484e+4, +9.359e+3, +1.364e+3)},
         302:{'type':'sf',
              'A':(+1.248e+1, +8.429e+2, -7.194e+2, +1.665e+2, +2.114e+2)},
         301:{'type':'sf',
              'A':(+1.010e+1, +3.349e+3, +1.034e+4, -1.269e+4, +3.023e+3)},
         300:{'type':'sf',
              'A':(+3.068e+0, +1.914e+2, +1.311e+3, -1.191e+3, +5.774e+2)},
         402:{'type':'sf',
              'A':(+3.009e+0, +1.194e+2, -1.716e+2, +9.982e+1, +9.528e+1)},
         403:{'type':'sf',
              'A':(+5.663e-1, +1.780e+1, -3.464e+1, +1.990e+1, +1.573e+1)},
         401:{'type':'sf',
              'A':(+2.226e+0, +4.009e+2, +3.283e+3, -3.644e+3, +1.904e+3)},
         400:{'type':'sf',
              'A':(+5.902e-1, +1.755e+1, +1.286e+1, +1.786e+1, +1.158e+2)},
         'ion':{'type':'ion',
              'A':(+2.104e-1, -1.750e-1, 2.994e-11,
                   +9.493e-1, -4.479e-1, -3.833e-1)}},

    310:{311:{'type':'da',
              'A':(+4.881e+2, +7.567e+2, -6.376e+3,
                   +1.258e+4, -7.062e+3, +1.652e+1)},
         411:{'type':'da',
              'A':(+7.079e+0, -9.037e-1, -1.830e+0,
                   +2.059e+1, -8.431e+0, +2.199e+0)},
         312:{'type':'df',
              'A':(+1.293e+2, -2.074e+1, -3.571e+2, +2.500e+2, +0.000e+0)},
         410:{'type':'df',
              'A':(+3.862e+1, -1.898e+2, +3.639e+2, -5.587e+1, +1.719e+1)},
         412:{'type':'df',
              'A':(+3.031e+1, +1.193e+2, +1.209e+2, -1.560e+2, +5.758e+1)},
         413:{'type':'df',
              'A':(+3.902e+1, +1.083e+2, +8.382e+2, -8.417e+2, +4.843e+1)},
         302:{'type':'sf',
              'A':(+1.545e+2, +4.931e+4, +4.578e+4, -9.484e+4, +6.629e+3)},
         301:{'type':'sf',
              'A':(+6.104e+1, -1.350e+2, +1.268e+2, -5.257e+1, +6.185e+0)},
         300:{'type':'sf',
              'A':(+1.731e+2, +2.350e+6, +5.044e+6, -7.305e+6, +3.601e+5)},
         402:{'type':'sf',
              'A':(+3.036e+0, -2.081e+3, +6.538e+5, -5.498e+5, +1.362e+5)},
         403:{'type':'sf',
              'A':(+9.155e-1, +6.187e+2, +2.079e+2, -6.677e+2, +3.049e+2)},
         401:{'type':'sf',
              'A':(+1.725e+0, +4.197e+2, +1.477e+3, -1.845e+3, +1.186e+3)},
         400:{'type':'sf',
              'A':(+9.802e-1, +7.696e+3, -2.354e+4, +4.408e+4, +1.801e+4)},
         'ion':{'type':'ion',
              'A':(+1.878e-1, -1.871e-1, +1.223e+0,
                   -3.805e+0, +8.412e+0, -5.872e+0)}},

    311:{312:{'type':'da',
              'A':(+9.796e+2, +1.371e+3, +8.389e+4,
                   -4.649e+5, +6.375e+5, +4.209e+1)},
         410:{'type':'da',
              'A':(+1.233e+2, +2.406e+1, -5.256e+2,
                   +1.274e+3, -6.444e+2, +2.301e+1)},
         412:{'type':'da',
              'A':(+3.295e+2, +6.359e+1, -1.630e+3,
                   +4.159e+3, -2.512e+3, +2.522e+1)},
         413:{'type':'df',
              'A':(+4.062e+2, +1.633e+3, +6.407e+3, -5.657e+3, +1.825e+2)},
         411:{'type':'df',
              'A':(+1.832e+2, -8.062e+2, +1.381e+3, -7.116e+2, +2.103e+0)},
         302:{'type':'sf',
              'A':(+6.039e+3, +4.209e+7, -1.969e+8, +2.637e+8, +2.223e+5)},
         301:{'type':'sf',
              'A':(+6.013e+3, -1.055e+4, +1.091e+4, -6.078e+3, +8.163e+2)},
         402:{'type':'sf',
              'A':(+7.376e+0, +2.988e+3, +8.026e+3, -7.799e+3, +1.065e+3)},
         403:{'type':'sf',
              'A':(+6.272e+1, +6.842e+3, +1.574e+3, -5.607e+3, +1.122e+3)},
         401:{'type':'sf',
              'A':(+2.776e+1, -8.087e+1, +3.210e+2, -2.668e+2, +2.334e+1)},
         400:{'type':'sf',
              'A':(+3.483e+0, +1.338e+3, +5.297e+3, -2.062e+3, +2.147e+3)},
         'ion':{'type':'ion',
              'A':(+2.694e-1, -2.606e-1, +6.476e-1,
                   -2.256e+0, +5.876e+0, -4.273e+0)}},

    312:{413:{'type':'da',
              'A':(+1.255e+3, +8.455e+2, -6.966e+3,
                   +1.319e+4, -6.781e+3, +2.291e+1)},
         411:{'type':'da',
              'A':(+2.639e+1, -8.708e+0, +8.497e+1,
                   +4.800e+0, -2.920e+1, +4.310e+0)},
         410:{'type':'df',
              'A':(+2.782e+1, +9.856e+1, +8.697e+2, +2.306e+3, +1.772e+2)},
         412:{'type':'df',
              'A':(+2.774e+2, -8.107e+2, +3.733e+3, -2.662e+3, +3.313e+1)},
         302:{'type':'sf',
               'A':(+1.136e+9,  +2.017e+12, -1.201e+15,
                    +1.669e+17, +1.343e+8)},
         301:{'type':'sf',
              'A':(+1.102e+5, -5.174e+5, +8.277e+5, -4.200e+5, +1.461e+4)},
         402:{'type':'sf',
              'A':(+4.723e+1, +1.223e+5, +2.166e+5, -2.717e+5, +1.935e+4)},
         403:{'type':'sf',
              'A':(+6.305e+1, +2.582e+4, -1.481e+4, -5.014e+3, +1.496e+3)},
         401:{'type':'sf',
              'A':(+0.000e+0, +2.958e+3, +6.343e+3, -9.301e+3, +9.406e+2)},
         400:{'type':'sf',
              'A':(+6.079e-1, +9.783e+2, +1.616e+3, -1.574e+3, +8.714e+2)},
         'ion':{'type':'ion',
              'A':(+8.034e-2, -7.667e-2, +8.839e-1,
                   -4.051e+0, +1.110e+1, -7.427e+0)}},

    410:{411:{'type':'da',
              'A':(+3.306e+3, -8.483e+3, +2.027e+4,
                   -1.869e+4, +6.912e+3, +2.733e+0)},
         412:{'type':'df',
              'A':(+5.093e+2, -1.954e+3, +2.489e+3, -1.035e+3, +0.000e+0)},
         413:{'type':'df',
              'A':(+1.054e+2, -1.972e+3, +2.347e+4, -2.137e+4, +9.322e+1)},
         402:{'type':'sf',
              'A':(+2.220e+2, +3.024e+6, +9.322e+6, -1.234e+7, +4.572e+5)},
         403:{'type':'sf',
              'A':(+4.678e+1, +7.677e+4, -1.273e+5, +6.421e+4, +5.849e+3)},
         401:{'type':'sf',
              'A':(+1.650e+2, +1.455e+6, -2.700e+6, +1.284e+6, +1.720e+5)},
         400:{'type':'sf',
              'A':(+3.429e+2, +9.919e+6, -7.244e+6, +3.127e+7, +1.147e+6)},
         'ion':{'type':'ion',
              'A':(+9.429e-2, -7.480e-2, +8.668e-1,
                   -3.637e+0, +8.681e+0, -5.816e+0)}},

    411:{412:{'type':'da',
              'A':(+3.462e+3, +8.765e+3, +5.011e+5,
                   -6.347e+6, +1.989e+7, +6.451e+1)},
         413:{'type':'df',
              'A':(+6.848e+2, -8.638e+4, +1.881e+7, -1.825e+7, +2.744e+4)},
         402:{'type':'sf',
              'A':(+1.466e+4, +8.679e+8, -3.528e+9, +4.055e+9, +4.533e+6)},
         403:{'type':'sf',
              'A':(+1.878e+4, +4.402e+7, -2.107e+8, +2.660e+8, +2.108e+5)},
         401:{'type':'sf',
              'A':(+1.482e+4, -4.752e+4, +3.964e+4, +3.244e+3, +2.200e+3)},
         'ion':{'type':'ion',
              'A':(+2.128e-1, -1.957e-1, +4.731e-1,
                   -1.800e+0, +3.198e+0, -2.596e+0)}},

    412:{413:{'type':'da',
              'A':(+2.884e+3, +2.423e+4, +1.663e+7,
                   -2.552e+8, +2.912e+9, +5.760e+2)},
         402:{'type':'sf',
              'A':(+7.367e+8, -2.854e+9, +5.369e+9, -3.233e+9, +6.737e+7)},
         403:{'type':'sf',
              'A':(+5.179e+7, -3.389e+8, +7.078e+8, -4.136e+8, +3.808e+6)},
         401:{'type':'sf',
              'A':(+3.467e+5, -1.223e+5, -1.174e+7, +2.974e+7, +7.585e+4)},
         'ion':{'type':'ion',
              'A':(+2.507e-2, -4.722e-3, +1.340e-1,
                   +7.719e-1, -4.388e-1, +1.245e-1)}},
    
    413:{403:{'type':'sf',
              'A':(+1.026e+10, +3.470e+13, -2.933e+16,
                   +5.666e+18, +6.300e+8)},
         401:{'type':'sf',
              'A':(+2.520e+5, -1.057e+6, -1.446e+6, +8.086e+6, +4.052e+4)},
         'ion':{'type':'ion',
              'A':(+6.742e-3, +4.431e-2, -8.945e-2,
                   +1.335e+0, +4.955e-1, -1.073e+0)}},

    401:{'ion':{'type':'ion',
              'A':(+1.807e-1, -1.724e-1, +2.448e-1,
                   -6.578e-1, +2.026e+0, -1.535e+0)}}
}

class Transition(object):
    def __init__(self, istate, fstate):
        self.istate = istate
        self.fstate = fstate
        try:
            self.transition = constants[istate][fstate]
            self.inverse = False
            self.undefined = False
        except KeyError:
            try:
                self.transition = constants[fstate][istate]
                self.inverse = True
                self.undefined = False
            except KeyError:
                self.undefined = True
        finally:
            self.dE = abs(states[fstate]['E'] - states[istate]['E'])

    def sigma(self, E):
        if self.undefined:
            return np.zeros(np.size(E))
        A = self.transition['A']
        Ei, Ef = states[self.istate]['E'], states[self.fstate]['E']
        gi, gf = states[self.istate]['g'], states[self.fstate]['g']
        
        if self.inverse:
            E = E + self.dE
        
        try:
            zindex = np.where(E < self.dE)[0][-1]
        except IndexError:
            zeros = np.array([])
        else:
            E = E[zindex + 1:]
            zeros = np.zeros((1, (zindex + 1)))
        x = E/self.dE
            
        if self.transition['type'] is 'ion':
            I = self.dE
            summed = 0.0
            for i in range(1,6):
                summed += A[i] * (1 - I/E)**i
            sigma = q**2 * 1e-13/(I*E) * (A[0]*log(E/I) + summed) * 1e-4
            return np.append(zeros, sigma)

        if self.transition['type'] is 'da':
            O = ((A[0]*log(x) + A[1] + A[2]/x + A[3]/x**2 + A[4]/x**3)
                  * ((x + 1) / (x + A[5])))

        elif self.transition['type'] is 'df':
            O = ((A[0] + A[1]/x + A[2]/x**2 + A[3]/x**3)
                  * (x**2 / (x**2 + A[4])))

        elif self.transition['type'] is 'sf':
            O = (A[0] + A[1]/x + A[2]/x**2 + A[3]/x**3) / (x**2 + A[4])

        #O = np.append(zeros, O)
        direct = pi * a0**2 * Ry/(gi*E) * O
        direct = np.append(zeros, direct)
        if self.inverse:
            return x/(x-1) * gf**2/gi * direct
        else:
            return direct
