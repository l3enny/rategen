import xsections.helium.ralchenko as xsections
import xsections.helium.nahar as nahar
from xsections.helium.states import states

import distributions
import numpy as np
from constants import q

temperatures = np.logspace(-1, np.log10(300), 1e2) * q

# Define the distribution to use and any inputs besides the temperature
distribution = distributions.drumax
kargs = {'x':1.0}

dump = 'combined'
comments = {'Cross-Sections':'(Ralchenko 2008), (Nahar 2010)',
            'Distribution':'Generalized Maxwellian',
            'x':kargs['x'],
            'Temperatures':'0.1-300 eV, log spacing, 100 points',
            'Compiler':'Ben Yee'}

elastic = False
