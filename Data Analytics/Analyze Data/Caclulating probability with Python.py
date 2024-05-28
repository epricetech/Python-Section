# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:30:04 2023

@author: geron
"""

# use the scipy.stats library with import and the bionom.pmf() function with 3 values 
#   x=the value of interest
#   n=the number of trials
#   p=the probability of success


import scipy.stats as stats

# value of interest
# change this
x = 3

# sample size
# change this
n = 10

# calculate probability
prob_1 = stats.binom.pmf(x, n, 0.5)
print(prob_1)



# PMF over a range  use the same import and function as above.  
# x= the value of interest    y =  sample size  p = probability of success

import scipy.stats as stats
 
# calculating P(2-4 heads) = P(2 heads) + P(3 heads) + P(4 heads) for flipping a coin 10 times
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5))


import scipy.stats as stats
 
# calculating P(less than 3 heads) = P(0 heads) + P(1 head) + P(2 heads) for flipping a coin 10 times
print(stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) + stats.binom.pmf(2, n=10, p=.5))


# When there are many possible values of interest, this task of adding up probabilities can be difficult.
#  If we want to know the probability of observing 8 or fewer heads from 10 coin flips,
#  we need to add up the values from 0 to 8:

import scipy.stats as stats
 
stats.binom.pmf(0, n = 10, p = 0.5) + stats.binom.pmf(1, n = 10, p = 0.5)
 + stats.binom.pmf(2, n = 10, p = 0.5)
 + stats.binom.pmf(3, n = 10, p = 0.5)
 + stats.binom.pmf(4, n = 10, p = 0.5)
 + stats.binom.pmf(5, n = 10, p = 0.5)
 + stats.binom.pmf(6, n = 10, p = 0.5)
 + stats.binom.pmf(7, n = 10, p = 0.5)
 + stats.binom.pmf(8, n = 10, p = 0.5)


# Now instead of summing up 9 values for the probabilities between 0 and 8 heads,
#  we can do 1 minus the sum of two values and get the same result:

import scipy.stats as stats
# less than or equal to 8
1 - (stats.binom.pmf(9, n=10, p=.5) + stats.binom.pmf(10, n=10, p=.5))



import scipy.stats as stats

## Checkpoint 1
prob_1 = stats.binom.pmf(4,10,0.5) + stats.binom.pmf(5,10,0.5) + stats.binom.pmf(6,10,0.5)
print(prob_1)

## Checkpoint 2
prob_2 = 1 - (stats.binom.pmf(0,10,0.5) + stats.binom.pmf(1,10,0.5) + stats.binom.pmf(2,10,0.5))
print(prob_2)



# CMF function cumulative distibution function - similar to pmf but sometimes easier to use.  binom.cdf() 
#  x = the value of interest.  looking for the probability of this value or less   n = sample size  p = probability of success



# Calculating the probability of observing between 4 and 8 heads from 10 fair coin flips can be thought of as
#  taking the difference of the value of the cumulative distribution function at 8 from the cumulative distribution
#  function at 3:
import scipy.stats as stats
 
print(stats.binom.cdf(8, 10, 0.5) - stats.binom.cdf(3, 10, 0.5))

# To calculate the probability of observing more than 6 heads from 10 fair coin flips we subtract the value of the 
# cumulative distribution function at 6 from 1. Mathematically, this looks like the following:
import scipy.stats as stats
print(1 - stats.binom.cdf(6, 10, 0.5))




import scipy.stats as stats

## Checkpoint 1
prob_1 = stats.binom.cdf(3,10,.5)
print(prob_1)

# compare to pmf code
print(stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) + stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5))


## Checkpoint 2
prob_2 = 1 - (stats.binom.cdf(5,10,.5))
print(prob_2)


## Checkpoint 3
prob_3 = stats.binom.cdf(5,10,.5) - stats.binom.cdf(1,10,.5)
print(prob_3)

# compare to pmf code
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5) + stats.binom.pmf(5, n=10, p=.5))



#  using the stats.norm.cdf() function
#  x = the value of interest  loc = the mean of the probability distibution   scale = the standard deviation of the probability distribution

# for women less thatn 175cm tall.  loc is 177.64 and scale is 8
import scipy.stats as stats

prob = stats.norm.cdf(175,167.64,8)
print(prob)

#  we can take the difference between 2 overlapping ranges to calcluate the probability that a random selection will be
# within a range of values for continous distributions.  

#  Example random observings women between 165cm and 175cm assuing the mean is 167.64 and median is 8

import scipy.stats as stats
# P(165 < X < 175) = P(X < 175) - P(X < 165)
# stats.norm.cdf(x, loc, scale) - stats.norm.cdf(x, loc, scale)
print(stats.norm.cdf(175, 167.74, 8) - stats.norm.cdf(165, 167.74, 8))


#  women taller than 172 cm
import scipy.stats as stats
 
# P(X > 172) = 1 - P(X < 172)
# 1 - stats.norm.cdf(x, loc, scale)
print(1 - stats.norm.cdf(172, 167.74, 8))

import scipy.stats as stats

## Checkpoint 1  Between 18 and 25
temp_prob_1 = stats.norm.cdf(25,20,3) - stats.norm.cdf(18,20,3)
print(temp_prob_1)

## Checkpoint 2  - any temp higher than 24
temp_prob_2 = 1 - (stats.norm.cdf(24,20,3))
print(temp_prob_2)


import scipy.stats as stats
import numpy as np

## Exercise 1
# sampling from a 6-sided die
die_6 = range(1, 7)
print(np.random.choice(die_6, size = 5, replace = True))


## Exercise 4 - binomial probability mass function
# 6 heads from 10 fair coin flips
print(stats.binom.pmf(6, 10, 0.5))


## Exercise 6 - binomial probability mass function
# 2 to 4 heads from 10 coin flips
# P(X = 2) + P(X = 3) + P(X = 4)
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5))

# 0 to 8 heads from 10 coin flips
# 1 - (P(X = 9) + P(X = 10))
print(1 - (stats.binom.pmf(9, n=10, p=.5) + stats.binom.pmf(10, n=10, p=.5)))


## Exercise 9 - binomial cumulative distribution function
# 6 or fewer heads from 10 coin flips
print(stats.binom.cdf(6, 10, 0.5))

# more than 6 heads from 10 coin flips
print(1 - stats.binom.cdf(6, 10, 0.5))

# between 4 and 8 heads from 10 coin flips
print(stats.binom.cdf(8, 10, 0.5) - stats.binom.cdf(3, 10, 0.5))


## Exercise 10 - normal distribution cumulative distribution function
# stats.norm.cdf(x, loc, scale)
# temperature being less than 14*C
  # x = 14, loc = 20, scale = 3
print(stats.norm.cdf(14, 20, 3))


# Exercise 11
# temperature being greater than 24*C
  # x = 24, loc = 20, scale = 3
print(1 - stats.norm.cdf(24, 20, 3))

# temperature being between 21*C and 25*C
  # x = 24, loc = 20, scale = 3
print(stats.norm.cdf(25, 20, 3) - stats.norm.cdf(21, 20, 3))








