import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import *

import distributions

f = distributions.maxwellian(8.773 * e)
E = np.linspace(0, 200) * e
eedf = f(E) * (E)**-0.5 * e**1.5

plt.semilogy(E, f(E))
plt.semilogy(E / e, eedf)
plt.legend(('Original', 'Corrected'))
plt.axis([0, 200, 1e-6, 1e-1])
plt.show()
