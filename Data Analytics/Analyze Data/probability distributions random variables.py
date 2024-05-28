# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:41:10 2023

@author: geron
"""

import numpy as np
 
# 7 is not included in the range function
die_6 = range(1, 7)
 
rolls = np.random.choice(die_6, size = 2, replace = True)
 
print(rolls)



import numpy as np

# create 6 sided "die"
die_6 = range(1, 7)

# set number of rolls
num_rolls = 10

# roll the "die" the set amount of times
results_1 = np.random.choice(die_6, size = num_rolls, replace = True)
print(results_1)

# create 12-sided "die"
#die_12 =
die_12 = range(1,13)
# roll the 12-sided "die" 10 times
#results_2 = 
results_2 = np.random.choice(die_12, size=10, replace=True)
print(results_2)



