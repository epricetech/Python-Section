# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 12:19:10 2023

@author: geron
"""

import scipy.stats as stats

## Checkpoint 1
# calculate prob_15
prob_15 = stats.poisson.pmf(15,15)

print(prob_15)


## Checkpoint 
# calculate prob_7_to_9
prob_7_to_9 = stats.poisson.pmf(7,15) + stats.poisson.pmf(8,15) + stats.poisson.pmf(9,15)

# print prob_7_to_9
print(prob_7_to_9)



#  stats.poisson.cdf()  x = value of interest or less  y = expected value 

# if we want the calculate the probability of observing 6 or less rain events in 30 days.  expected is 10 events
import scipy.stats as stats
# expected value = 10, probability of observing 6 or less
stats.poisson.cdf(6, 10)


import scipy.stats as stats
# expected value = 10, probability of observing 12 or more
1 - stats.poisson.cdf(11, 10)


import scipy.stats as stats
# expected value = 10, probability of observing between 12 and 18
stats.poisson.cdf(18, 10) - stats.poisson.cdf(11, 10)



import scipy.stats as stats

## Checkpoint 1
# calculate prob_more_than_20
prob_more_than_20 = 1 - stats.poisson.cdf(20,15)

# print prob_more_than_20
print(prob_more_than_20)
## Checkpoint 
# calculate prob_17_to_21
prob_17_to_21 = stats.poisson.cdf(21,15) - stats.poisson.cdf(16,15)

# print prob_17_to_21
print(prob_17_to_21)



#  poisson.rvs() lets you creat random values.  x= expected value    size = sample size
#can use rvs.mean() to find the expected value

import scipy.stats as stats
import codecademylib3

from histogram_function import histogram_function

## Checkpoint 1
# lambda = 15, 1000 random draws 
rand_vars = stats.poisson.rvs(15, size=1000)

## Checkpoint 2
# print the mean of rand_vars
print(rand_vars.mean())

## Checkpoint 3
histogram_function(rand_vars)


#  Finding the spread of the poisson distribution

import scipy.stats as stats
import numpy as np
 
rand_vars = stats.poisson.rvs(4, size = 1000)
print(np.var(rand_vars))


import scipy.stats as stats
 
rand_vars = stats.poisson.rvs(4, size = 1000)
 
print(min(rand_vars), max(rand_vars))



import scipy.stats as stats
import numpy as np

## For checkpoints 1 and 2
# 5000 draws, lambda = 7
rand_vars_7 = stats.poisson.rvs(7, size = 5000)

## Checkpoint 1
# print variance of rand_vars_7
print(np.var(rand_vars_7))

## Checkpoint 2
# print minimum and maximum of rand_vars_7
print(min(rand_vars_7), max(rand_vars_7))

## For checkpoints 3 and 4
# 5000 draws, lambda = 17
rand_vars_17 = stats.poisson.rvs(17, size = 5000)

## Checkpoint 3
# print variance of rand_vars_17
print(np.var(rand_vars_17))

## Checkpoint 4
# print minimum and maximum of rand_vars_17
print(min(rand_vars_17), max(rand_vars_17))


import scipy.stats as stats
import numpy as np

## Checkpoint 1
expected_bonus = 75000 * .08
print(expected_bonus)

## Checkpoint 2
num_goals = stats.poisson.rvs(4, size=100)


## Checkpoint 3
print(np.var(num_goals))

## Checkpoint 4
num_goals_2 = num_goals * 2







