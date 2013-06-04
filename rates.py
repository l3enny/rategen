from scipy.interpolate import UnivariateSpline
import numpy as np


class Rates(object):

    def __init__(self, temperatures, splines, comments=None):
        #if len(rates) != len(temperatures):
        #   raise ValueError('There must be an equal number of rate tables and',
        #   'temperatures.')
        self.splines = splines
        self.temperatures = temperatures
        self.comments = comments

    def rate(self, Te, i, f):
        #TODO: Store splines in memory for speedup
        return self.splines[i, f]

    def km(self, Te):
        #TODO: Store splines in memory for speedup
        return self.splines[0](Te)

    def Ae(self, Te):
        output = np.zeros(self.splines.shape)
        for i in range(self.splines.shape[0]):
            for j in range(self.splines.shape[1]):
                output[i, j] = self.splines[i, j](Te)
        return output
