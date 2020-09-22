#!/usr/bin/env python
"""Problem Set 1 Code for QCB505 Fall 2020


"""

import numpy as np
import matplotlib.pyplot as plt

__author__ = "Scott Wolf"
__date__ = "20200908"
__credits__ = ["Scott Wolf"]
__version__ = "1"
__status__ = "Prototype"
__url__ = "https://www.dropbox.com/sh/jauik83zfg0rtfe/AACugg-_9g4Mfo2fPIUq_zQea?dl=0"

L = 5
kappa = 1
beta = 0.5
Nsteps = 100000
EE = np.zeros((Nsteps, 1))
S = np.zeros((Nsteps, 1))

for t in range(1, Nsteps):
    sold = S[t - 1]
    Eold = (kappa / 2) * ((sold / L) ** 2)
    snew = sold.copy()
    step = np.sign(np.random.normal())
    snew = sold + step
    Enew = (kappa / 2) * ((snew / L) ** 2)
    if np.exp(-beta * (Enew - Eold)) > np.random.uniform():
        S[t] = snew
        EE[t] = Enew
    else:
        S[t] = sold
        EE[t] = Eold

plt.hist(np.sum(S, axis=1))
plt.show()

plt.plot(EE[0:1000])
plt.show()

# Section 2

N = 100
Nsteps = 10000
s = np.zeros((Nsteps, N))
s[0, ] = np.sign(np.random.randn(N))
h = 1
beta = 2
EE = np.zeros(Nsteps)

for t in range(1,Nsteps):
    sold = s[t - 1,]
    Eold = -h * np.sum(sold)
    snew = sold.copy()
    flip = np.random.choice(100)
    snew[flip] = -sold[flip]
    Enew = -h * np.sum(snew)
    if np.exp(-beta * (Enew - Eold)) > np.random.rand(1):
        s[t,] = snew
        EE[t] = Enew
    else:
        s[t,] = sold
        EE[t] = Eold

plt.hist(np.sum(s, axis=1))
plt.show()

plt.plot(EE/N)
plt.show()

# Section 3

L = 10
N = L**2
nn = np.zeros((L,L))
for i in range(0,L):
    for j in range(0,L):
        nn[i,j] = (i-1)*L +(j-1) + 1