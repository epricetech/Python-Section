# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:17:34 2023

@author: geron
"""

import numpy as np
import pandas as pd
from scipy.stats import binom_test

def simulation_binomial_test(observed_successes, n, p):
  #initialize null_outcomes
  null_outcomes = []
  
  #generate the simulated null distribution
  for i in range(10000):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[p, 1-p])
    num_purchased = np.sum(simulated_monthly_visitors == 'y')
    null_outcomes.append(num_purchased)

  #calculate a 1-sided p-value
  null_outcomes = np.array(null_outcomes)
  p_value = np.sum(null_outcomes <= observed_successes)/len(null_outcomes) 
  
  #return the p-value
  return p_value

#Test your function below by uncommenting the code below. You should see that your simulation function gives you a very similar answer to the binom_test function from scipy:

p_value1 = simulation_binomial_test(45, 500, .1)
print("simulation p-value: ", p_value1)

p_value2 = binom_test(45, 500, .1, alternative = 'less')
print("binom_test p-value: ", p_value2)


# Output:
# simulation p-value:  0.2585
# binom_test p-value:  0.25468926056232155


# SciPy has a function called binom_test(), which performs a binomial test for you. 
# The default alternative hypothesis for the binom_test() function is two-sided,
#  but this can be changed using the alternative parameter (eg., alternative = 'less' will run a one-sided lower tail test).

# binom_test() requires three inputs, the number of observed successes, the number of total trials, 
# and an expected probability of success. For example, with 10 flips of a fair coin (trials), the expected
#  probability of heads is 0.5. Let’s imagine we get 2 heads (observed successes) in 10 flips. 
#  Is the coin weighted? The function call for this binomial test would look like:
    

from scipy import binom_test
p_value = binom_test(2, n=10, p=0.5)
print(p_value) #output: 0.109


import numpy as np
import pandas as pd
from scipy.stats import binom_test

# calculate p_value_2sided here:
p_value_2sided = binom_test(41,n=500,p=.1)
print(p_value_2sided)
# calculate p_value_1sided here:
p_value_1sided = binom_test(41, 500, .1, alternative = 'less')
print(p_value_1sided)


# Output:
# 0.20456397700678308
# 0.1001135269756488