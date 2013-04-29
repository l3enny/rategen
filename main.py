import rate
from settings import *
import cPickle
import pprint
import test

output = []
for temperature in temperatures:
    eedf = distribution(temperature, **kargs)
    output.append({})
    for i in states:
        output[-1][i] = {}
        for f in states:
            transition = xsections.Transition(i, f)
            K = rate.rate(transition, eedf)
            output[-1][i][f] = K

ralchenko = test.Rates(temperatures, output)
with open('ralchenko.pickle', mode='w') as f:
    p = cPickle.Pickler(f, protocol=2)
    p.dump(ralchenko)

#with open(dump + '_rate.txt', mode='w') as f:
#    printer = pprint.PrettyPrinter(indent=2, stream=f)
#    printer.pprint(output)

#with open(dump + '_temps.txt', mode='w') as f:
#    f.write(repr(temperatures))
