# Standard library modules
import cPickle

# Included packages
from constants import kB
import convolve
import rates

# Import settings: temperatures, distribution, kargs, dump, comments
import settings

output = []
for temperature in settings.temperatures:
    eedf = settings.distribution(temperature, **settings.kargs)
    output.append({})
    print "Calculating at temperature:", temperature
    for i in settings.states:
        output[-1][i] = {}
        for f in settings.states:
            transition = settings.xsections.Transition(i, f)
            K = convolve.rate(transition, eedf)
            output[-1][i][f] = K

print "output:", output
ralchenko = rates.Rates(settings.temperatures/kB, output, settings.comments)
with open('ralchenko.pickle', mode='w') as f:
    p = cPickle.Pickler(f, protocol=2)
    p.dump(ralchenko)
