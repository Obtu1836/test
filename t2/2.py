import numpy as np
from numpy.linalg import norm 

x=np.random.rand(5)
data=np.random.rand(10).reshape(2,5)

p=data[:,None]-data

print(p)
