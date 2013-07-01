from scipy.interpolate import UnivariateSpline
from scipy.interpolate import interp1d

class Rates(object):

    def __init__(self, temperatures, rates, comments=None):
        if len(rates) != len(temperatures):
            raise ValueError('There must be an equal number of rate tables and',
            'temperatures.')
        self.rates = rates
        self.temperatures = temperatures
        self.comments = comments

    def rate(self, Te, i, f):
        select = []
        for table in self.rates:
            select.append(table[i][f])
        #spline = UnivariateSpline(self.temperatures, select, s=0, k=2)
        func = interp1d(self.temperatures, select, kind='cubic')
        return func(Te)

    def km(self, Te):
        #spline = UnivariateSpline(self.temperatures, self.rates, s=0, k=2)
        func = interp1d(self.temperatures, select, kind='cubic')
        return func(Te)
