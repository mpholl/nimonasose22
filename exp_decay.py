import numpy as np
import matplotlib.pyplot as plt
from euler import *

def exp_decay(x, a):
    return -a*x

# numerical parameter
h = 0.5
# initial condition
xs = [0.5]
ts = [0]

# model parameter
alpha = 1.

pars = [alpha]

while ts[-1]<7:
    xs += [euler_step(xs[-1], exp_decay, h, pars)]
    ts += [ts[-1] + h]

plt.plot(ts, xs)
plt.show()

