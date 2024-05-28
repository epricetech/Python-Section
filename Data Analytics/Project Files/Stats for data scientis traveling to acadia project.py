# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:35:57 2023

@author: geron
"""

import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")
#Step5  - figure picks the size of graph and subplot describes the layout
plt.figure(1)
plt.subplot(211)
# Plot the histograms
plt.hist(flights, range=(0,365),bins=365)
plt.title('Weekday Frequency of Customers')
plt.xlabel('Hours - 1 hr sections')
plt.ylabel('Count')

# Step 6
plt.subplot(212)
plt.hist(in_bloom, range=(0,365), bins=365)
#can also add title and lables here if need
plt.show()