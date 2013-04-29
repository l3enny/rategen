# Standard library modules
import cPickle

# Included packages
from constants import kB
import convolve
import rates
import settings

output = []
for temperature in settings.temperatures:
    eedf = settings.distribution(temperature, **settings.kargs)
    print "Calculating at temperature:", temperature
    if elastic:
        K = convolve.rate2(settings.sigma, eedf)
    else:
        output.append({})
        for i in settings.states:
            output[-1][i] = {}
            for f in settings.states:
                transition = settings.xsections.Transition(i, f)
                K = convolve.rate(transition, eedf)
                output[-1][i][f] = K

container = rates.Rates(settings.temperatures/kB, output, settings.comments)
with open(dump + '.pickle', mode='w') as f:
    p = cPickle.Pickler(f, protocol=2)
    p.dump(container)
