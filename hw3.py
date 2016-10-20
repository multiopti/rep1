#!/usr/bin/env python
#import sys, math # load system and math module
#from math import *
import numpy as np
import matplotlib.pyplot as plt
import random

from scipy import signal

#t1 = np.linspace(0, 200, 200, endpoint=False)
#plt.plot(t1, 100*signal.square(2 * np.pi * 0.05 * t1))


#import time
#time.sleep(5) # delays for 5 seconds

final_p = 1000
sampling_t = 10

t = np.arange(0.0, final_p, sampling_t)
u = signal.sawtooth(2 * np.pi * 0.005 * t)
y = np.zeros(len(t))

for i in range(1,int(len(t)/2)):
    y[i] = 0.9*y[i-1] + 2*u[i-1] + random.uniform(-1,1)

for i in range(int(1+len(t)/2),len(t)):
    y[i] = 0.9*y[i-1] + 3*u[i-1] + random.uniform(-1,1)

#y = math.sin(2*pi*t)

# red dashes, blue squares and green triangles
plt.plot(t, y)
plt.show()
