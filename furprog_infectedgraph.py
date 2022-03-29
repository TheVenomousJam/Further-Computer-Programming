# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:17:47 2022

@author: jacke
"""

from matplotlib import pyplot as plt
import random
pop = 1000000
x = [0]
y = [100000]
infected = [1]
r= 1.4

for i in range(1,100):
    
     x.append(i)
     infected.append(infected[i-1]*r)
     y.append(y[i-1]-infected[i-1])
     
     # Mention x and y limits to define their range
     plt.xlim(0, 100)
     plt.ylim(0, 100000)
       
     # Ploting graph
     plt.plot(x, y, color = 'red')
     plt.pause(.1)
   
plt.show()

#want formula for sus over time 
#1,2,4