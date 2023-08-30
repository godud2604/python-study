# %%
import numpy as np

# %%
# Why it is useful: Memory-efficient container that provides fast numerical operations.
L = range(1000)
# %timeit [i**2 for i in L]
a = np.arange(1000)
# %timeit a**2

# %% 1-D
a = np.array([0, 1, 2, 3])
print(a)

print(a.ndim) # 1
print(a.shape) # (4,)
print(len(a)) # 4
# %% 2-D, 3-D, ...
b = np.array([[0, 1, 2], [3, 4, 5]]) # 2 x 3 array
print(b)

print(b.ndim) # 2
print(b.shape) # (2, 3)
print(len(b)) # 2 => returns the size of the first dimension

c = np.array([[[1], [2]], [[3], [4]]])
print(c)
print(c.ndim) # 3
print(c.shape) (2, 2, 1)

# %% Functions for creating arrays
## Evenly spaced:
a = np.arange(10) # 0, ... , n-1
print(a)

b = np.arange(1, 9, 2)
print(b)

## or by number of points
c = np.linspace(0, 1, 6)  # start, end, num-points
print(c)

d = np.linspace(0, 1, 5, endpoint=False) 
print(d) # [0.  0.2 0.4 0.6 0.8]

## Common arrays:
a = np.ones((3, 3))
print(a)

b = np.zeros((2, 2))
print(b)

c = np.eye(3)
print(c)

d = np.diag(np.array([1, 2, 3, 4]))
print(d)
# %% random numbers
a = np.random.rand(4) # uniform in [0, 1]
print(a) # [0.60199935 0.89155816 0.02657054 0.67826607]

b = np.random.randn(4) # Gaussian
print(b)

np.random.seed(1234)

# %%
