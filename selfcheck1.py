import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
c = np.concatenate((a, b), axis=0)
print(c)
t = a
a = np.arange(1,20,2).reshape(5,2)
print(a)
b = np.reshape(np.arange(1, 21, 2), (5, 2), order='T')
print(b)