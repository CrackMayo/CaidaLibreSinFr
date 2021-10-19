# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:02:25 2018

@author: CrackMayo
"""
import numpy as np
import matplotlib.pyplot as plt

y=10
v=0
t=0
g=3.721
dt=0.01
t=np.arange(0,1,dt)
y=-g*t**2/2+v*t+y
plt.plot(t,y)
plt.show()