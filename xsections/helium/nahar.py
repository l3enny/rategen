import re

import numpy as np
from scipy.constants import *

# Notify user that the recombination coefficents are for Maxwellian temperatures
print "***NOTE*** Using Maxwellian recombination rate coefficients!"

# Skip to this part of the file to simplify parsing.
start = 299

# Regex patterns for the state
pattern = re.compile(r"(\d)(\d{2})(\d)(\d{2})(\d{2})\.(\d{2})(\d)(\d)")

# Load file into memory
with open("he1.rrc.ls.txt", mode="r") as f:
    lines = f.readlines()

temperatures = []
states = []

for line in lines[start:start+13]:
    items = line.split()
    for i in items:
        if "(K)" in i:
            temperatures.append(i.split("(K)")[0])

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
        sigma = [1e-6 * float(i) for i in sigma]
        lindex += 12
    lindex += 1

def rrc(state, temperature):
    state = '0' + str(state)
    func = interp1d(temperatures, sigma[states.index(state)], kind='cubic')
    return func(temperature)
