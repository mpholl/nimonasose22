import numpy as np
import matplotlib.pyplot as plt
from euler import *

def harm_oszi(x, omega):
    pos = x[0]
    vel = x[1]

    res1 = vel
    res2 = -omega**2*pos
    return np.array([res1, res2])

# numerical parameter
h = 0.5
# initial condition
xs = [np.array([0, 1])]
ts = [0]

# model parameter
omega = 1.

pars = [omega]

while ts[-1]<20:
    xs += [euler_step(xs[-1], harm_oszi, h, pars)]
    ts += [ts[-1] + h]

xs = np.array(xs)
plt.plot(ts, xs)
plt.show()
