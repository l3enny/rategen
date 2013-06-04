import xsections.helium.ralchenko as xsections
import distributions
import numpy as np
from xsections.helium.states import states
from constants import q

temperatures = np.logspace(-1, 2) * q
order = sorted(states.keys(), key=lambda x: states[x]['E'])

# Define the distribution to use and any inputs besides the temperature
distribution = distributions.drumax
kargs = {'x':0.5}

dump = 'ralchenko_0p5'
comments = {'Cross-Sections':'Ralchenko, 2008',
            'Distribution':'Generalized Maxwellian',
            'x':kargs['x'],
            'Temperatures':'0.1-100 eV, log spacing, 50 points',
            'Author':'Ben Yee'}

elastic = False
