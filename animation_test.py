# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:23:49 2022

@author: josste
"""

import matplotlib.pyplot as plt
import random

x = []
y = []

for _ in range(0,40):
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))
    
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.scatter(x, y, color='green')
    plt.pause(0.0001)
    
plt.show()