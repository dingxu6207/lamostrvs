# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 08:55:40 2021

@author: dingxu
"""

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy import signal


path = 'E:\\shunbianyuan\\phometry\\pipelinecode\\lamostrvs\\med708385622\\'
file = 'med-58478-TD010605N031628K01_sp13-180.fits.gz'
filename = path+file

hdulist = fits.open(filename)
hdulist.info()
print(hdulist[0].header)
print(hdulist[0].header['DATE-END'])

i = 2
col = hdulist[i].columns

print (col.names)

tbdata = hdulist[i].data
fluxdata = tbdata['FLUX']
wave = tbdata['LOGLAM']
    
wavelist = 10**wave

plt.plot(wavelist, fluxdata)

waveflux = [wavelist, fluxdata]

npwaveflux = np.array(waveflux)

np.savetxt('waveflux8.txt', npwaveflux.T)

from astropy.time import Time
times = [hdulist[0].header['DATE-END']]
t = Time(times, format='isot', scale='utc')
print(t.jd[0])