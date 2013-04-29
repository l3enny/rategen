import cPickle

with open('ralchenko.pickle', mode='r') as f:
    u = cPickle.Unpickler(f)
    coeffs = u.load()

print coeffs.rate(1.6021e-19, 100, 201)
