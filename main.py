# Standard library modules
import cPickle

# Included packages
import convolve
import rates

# Import settings: temperatures, distribution, kargs, dump, comments
import settings

output = []
for temperature in settings.temperatures:
    eedf = settings.distribution(temperature, **settings.kargs)
    output.append({})
    for i in states:
        output[-1][i] = {}
        for f in states:
            transition = xsections.Transition(i, f)
            K = rate.rate(transition, eedf)
            output[-1][i][f] = K

ralchenko = rates.Rates(temperatures, output, settings.comments)
with open('ralchenko.pickle', mode='w') as f:
    p = cPickle.Pickler(f, protocol=2)
    p.dump(ralchenko)
