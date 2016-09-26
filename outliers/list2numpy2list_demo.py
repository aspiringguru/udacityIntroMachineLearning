import numpy as np
from itertools import chain

a = [1,2,3,4,5,6,7,8,9]
print type(a), len(a), a
npa = np.asarray(a)
print type(npa), npa.shape, "\n", npa
npa = npa.reshape((3, 3))
print type(npa), npa.shape, "\n", npa
a = list(chain.from_iterable(npa))
print type(a), len(a), a
