import xsections.helium.pack.sigma as sigma
import distributions
import numpy as np
from constants import q

temperatures = np.logspace(-1, 2) * q

# Define the distribution to use and any inputs besides the temperature
distribution = distributions.drumax
kargs = {'x':0.5}

dump = 'pack'
comments = {'Cross-Sections':'Pack, 1992',
            'Distribution':'Generalized Maxwellian',
            'x':kargs['x'],
            'Temperatures':'0.1-100 eV, log spacing, 50 points',
            'Author':'Ben Yee'}
elastic = True
