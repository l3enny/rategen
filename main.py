# Third-party modules
from scipy.interpolate import UnivariateSpline
import numpy as np

# Standard library modules
import cPickle

# Included packages
from constants import kB
import convolve
import rates
from settings import ralchenko_0p5 as settings

order = settings.order
dim = len(settings.states)

if settings.elastic:
    K = []
    output = []
    for temperature in settings.temperatures:
        eedf = settings.distribution(temperature, **settings.kargs)
        K.append(convolve.rate2(settings.sigma, eedf))
    output.append(UnivariteSpline(temperatures/kB, K, s=0, k=2))
else:
    output = np.zeros((dim, dim), dtype=object)
    for i in range(dim):
        for j in range(dim):
            print "State (%s, %s)" % (str(order[i]), str(order[j]))
            transition = settings.xsections.Transition(order[i], order[j])
            K = []
            for temperature in settings.temperatures:
                eedf = settings.distribution(temperature, **settings.kargs)
                K.append(convolve.rate(transition, eedf))
            output[i][j] = UnivariateSpline(settings.temperatures/kB, K, s=0, k=2)

container = rates.Rates(settings.temperatures/kB, output, settings.comments)

with open(settings.dump + '.pickle', mode='w') as f:
    p = cPickle.Pickler(f, protocol=cPickle.HIGHEST_PROTOCOL)
    p.dump(container)
