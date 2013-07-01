# Standard library modules
import cPickle

# Third party packages
from scipy.constants import *

# Included packages
import convolve
import rates

from settings import combined as settings

output = []
for temperature in settings.temperatures:
    eedf = settings.distribution(temperature, **settings.kargs)
    print "Calculating at temperature:", temperature
    if settings.elastic:
        K = convolve.rate2(settings.sigma, eedf)
        output.append(K)
    else:
        output.append({})
        for i in settings.states:
            output[-1][i] = {}
            for f in settings.states:
                if i == 'ion':
                    K = settings.nahar.rrc(f, temperature)
                else:
                    transition = settings.xsections.Transition(i, f)
                    K = convolve.rate(transition, eedf)
                output[-1][i][f] = K

container = rates.Rates(settings.temperatures/k, output, settings.comments)

with open(settings.dump + '.pickle', mode='w') as f:
    p = cPickle.Pickler(f, protocol=2)
    p.dump(container)
