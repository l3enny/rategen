from xsections.helium.pack import sigma
import distributions
import numpy as np
from constants import q

temperatures = np.logspace(-1, 2) * q

# Define the distribution to use and any inputs besides the temperature
distribution = distributions.drumax
kargs = {'x':1.0}

dump = 'pack_m'
comments = {'Cross-Sections':'Pack, 1992',
            'Distribution':'Generalized Maxwellian',
            'x':kargs['x'],
            'Temperatures':'0.1-100 eV, log spacing, 50 points',
            'Author':'Ben Yee'}
elastic = True
