# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 12:08:51 2021

@author: dingxu
"""

import numpy as np
import matplotlib.pylab as plt
from PyAstronomy import pyasl


spcdata1 = np.loadtxt('npnormdata0.txt')
spcdata1 = spcdata1.T
spcdata1 = spcdata1[spcdata1[:,0]>6420]
spcdata1 = spcdata1[spcdata1[:,0]<6700]

spcdata2 = np.loadtxt('npnormdata3.txt')
spcdata2 = spcdata2.T
spcdata2 = spcdata2[spcdata2[:,0]>6420] #[1500:2500,:]
spcdata2 = spcdata2[spcdata2[:,0]<6700]

plt.figure(0)
plt.plot(spcdata1[:,0], spcdata1[:,1],'r')
plt.plot(spcdata2[:,0], spcdata2[:,1],'g')

dw = spcdata1[:,0] 
df = spcdata1[:,1]

tw = spcdata2[:,0]
tf = spcdata2[:,1]

rv, cc = pyasl.crosscorrRV(dw, df, tw, tf, -160., 160., 0.1, skipedge=26)

# Find the index of maximum cross-correlation function
maxind = np.argmax(cc)

print("Cross-correlation function is maximized at dRV = ", rv[maxind], " km/s")
if (rv[maxind] > 0.0):
    print("  A red-shift with respect to the template")
else:
    print("  A blue-shift with respect to the template")
    
plt.figure(1)
plt.plot(rv, cc, 'bp-')
plt.plot(rv[maxind], cc[maxind], 'ro')
plt.show()

x1 = 6564.18
x2 = 6564.32

v = (x2-x1)*299792.458/x1

print(v)