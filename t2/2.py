import numpy as np
from numpy.linalg import norm 

x=np.random.rand(5)
data=np.random.rand(15).reshape(3,5)

p=norm(data[:,None]-data,axis=2)

print(p)
