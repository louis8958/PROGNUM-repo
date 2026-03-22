#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.constants

fig, (ax1, ax2) = plt.subplots(2)

def gauss(x, A, x0, sigma, z0):
    """Gaussian Function"""
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

#Plotting the gauss function from a value of x from -20 to 20
A = 1.0
x0 = 0.0
sig = 2.0
z0 = 0.0
x = np.linspace(-20, 20, 200)
ax1.plot(x, gauss(x, A, x0, sig, z0), color = 'red', label = 'Coursework gaussian function')
fig.suptitle('Gaussian Functions')
fig.supxlabel('X')
fig.supylabel('Y')

#Calculation of the integral using the quad method
Area = scipy.integrate.quad(gauss, 0, 2.5, args=(A, x0, sig, z0))
print(f'The value of the area using the quad method is {Area}')
ax1.fill_between(np.linspace(0, 2.5, 200), gauss(np.linspace(0, 2.5, 200), A, x0, sig, z0), color = 'pink', label = 'Area value is about {}'.format((Area[0])))
Areainf = scipy.integrate.quad(gauss, -np.inf, np.inf, args=(A, x0, sig, z0))
print(Areainf)

Calc1 = A*sig*sqrt(2*pi)
print(f'The calculated from the equation {Calc1} is equal to that calculated with quad {Areainf[0]}')


A = float(input('The value of A is '))
x0 = float(input('The value of x0 is '))
sig = float(input('The value of sog is '))
z0 = float(input('The value of z0 is '))
limmin = float(input('The value of min lim is '))
limmax = float(input('The value of max lim is '))

def gaussarea(x, A, x0, sigma, z0):
    """Gaussian Function"""
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

x = np.linspace(limmin, limmax, 200)
ax2.plot(x, gauss(x, A, x0, sig, z0), color = 'orange', label = 'User gaussian function')
#Calculation of the integral using the quad method
Area2 = scipy.integrate.quad(gaussarea, limmin, limmax, args=(A, x0, sig, z0))
print(f'The value of the area using the quad method is {Area2}')
ax2.fill_between(np.linspace(limmin, limmax, 200), gauss(np.linspace(limmin, limmax, 200), A, x0, sig, z0), color = 'purple', label = 'Area value is about {}'.format((Area2[0])))
fig.legend()


# In[ ]:




