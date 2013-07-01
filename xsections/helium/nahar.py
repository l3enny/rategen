import re

import numpy as np
from scipy.constants import *
from scipy.interpolate import interp1d

# Notify user that the recombination coefficents are for Maxwellian temperatures
print "***NOTE*** Using Maxwellian recombination rate coefficients!"

# Skip to this part of the file to simplify parsing.
start = 298

# Regex patterns for the state
pattern = re.compile(r"(\d)(\d{2})(\d)(\d{2})(\d{2})\.(\d{2})(\d)(\d)")

# Load file into memory
with open("he1.rrc.ls.txt", mode="r") as f:
    lines = f.readlines()

temperatures = []
states = []
sigmas = []

# Read in the temperatures for each reaction rate
for line in lines[start:start+14]:
    items = line.split()
    for i in items:
        if "(K)" in i:
            temperatures.append(float(i.split("(K)")[0]))

# Read in the reaction rates for each temperature
for lindex in range(start + 13, len(lines)):
    items = lines[lindex].split()
    if items:
        try:
            S, LL, p, ZZ, NN, nn, l, f = filter(None, pattern.split(items[0]))
            S = str((int(S) - 1) / 2)
        except ValueError:
            lindex += 1
            continue
        states.append(''.join((nn, S, l)))
        tmp = lines[lindex:lindex + 12]
        tmp = [i.split() for i in tmp]
        sigma = sum(tmp, [])[2:]
        sigma = np.array([float(i) for i in sigma]) * 1e-6
        sigmas.append(sigma)
        lindex += 12
    lindex += 1

# Provide method to access interpolation of values
def rrc(state, temperature):
    state = '0' + str(state)
    if state == '0100':
        state = '0000'
    func = interp1d(temperatures, sigmas[states.index(state)], kind='cubic')
    return func(temperature)
