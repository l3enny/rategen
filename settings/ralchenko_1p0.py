import xsections.helium.ralchenko as xsections
import distributions
import numpy as np
from xsections.helium.states import states
from constants import q

temperatures = np.logspace(-1, 2) * q

# Define the distribution to use and any inputs besides the temperature
distribution = distributions.drumax
kargs = {'x':1.0}

dump = 'ralchenko_x=1.0'
comments = {'Cross-Sections':'Ralchenko, 2008',
            'Distribution':'Generalized Maxwellian',
            'x':kargs['x'],
            'Temperatures':'0.1-100 eV, log spacing, 50 points',
            'Author':'Ben Yee'}

elastic = False
