# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:21:43 2018

@author: Tsende
"""
# Maxwell-Boltzmann distribution

import numpy as np
import matplotlib.pyplot as plt

m1 = 132*1.66054e-27

T1 = 300
kb = 1.38064852e-23
alpha1 = np.sqrt(2*kb*T1/m1)

v = np.arange(0,1000,1)
Pv1 = (4/(np.sqrt(np.pi)*alpha1**3))*(v**2)*np.exp(-(v/alpha1)**2)
Flux1 = v*Pv1

m2 = 40*1.66054e-27

T2 = 300
kb = 1.38064852e-23
alpha2 = np.sqrt(2*kb*T2/m2)


Pv2 = (4/(np.sqrt(np.pi)*alpha2**3))*(v**2)*np.exp(-(v/alpha2)**2)
Flux2 = v*Pv2

plt.plot(v,Pv1,v,Pv2)
plt.xlabel('Velocity (m/s)')
plt.ylabel('Flux')


plt.grid(which='both')