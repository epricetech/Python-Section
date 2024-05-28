# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:14:54 2023

@author: geron
"""

# 1.
# In the workspace, you can see the sampling distribution of the maximum. 
# The mean of the distribution is not equal to the maximum of the population, showing that it is a biased estimator.

# Let’s look at another example. Edit the function app_statistic() so that it returns the variance 
# using the NumPy function np.var(). (You can change the string as well to update the title of your plots.)

# Based on the resulting mean of the sampling distribution, would you say that variance is a biased or unbiased estimator?

# Checkpoint 2 Passed

# Hint
# Once you edit the function, it should look something like:

# app_stat_text = "Variance"
# def app_statistic(x):
#     return np.var(x)
# Since the mean of the sampling distribution of the variance is not equal to the variance of the population, 
# it is a biased estimator. However, you may notice that it is close! If we set ddof=1 in the np.var() function, 
# we can calculate sample variance, which is very similar to “population variance” except 
# that the formula has sample_size - 1 in the denominator instead of just sample_size. Sample variance is an 
# unbiased estimator of population variance.

# Don’t forget to scroll down to see the second plot.

# 2.
# Change the statistic to mean using the np.mean() NumPy function. Does what you see correspond with what we 
# know about biased and unbiased estimators?

# Feel free to try out other statistics in the app_statistic() function!

# Checkpoint 3 Passed

# Hint
# Once you edit the function, it should look something like:

# app_stat_text = "Mean"
# def app_statistic(x):
#     return np.mean(x)
# The mean is an unbiased estimator because the mean of its sampling distribution is equal to the population 
# mean (in this case, equality will be approximate because we have simulated the sampling distribution). 
# We can see this in the simulation.


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import codecademylib3

app_stat_text = "Maximum"
def app_statistic(x):
    return np.mean(x)

### Below calculates the statistic for this population:
### You don't need to change anything below to pass the checkpoints
mean, std_dev = 50, 15
population = np.random.normal(mean, std_dev, 1000)

pop_statistic = round(app_statistic(population),2)

sns.histplot(population, stat = 'density')
plt.axvline(pop_statistic,color='r',linestyle='dashed')
plt.title(f"Population {app_stat_text}: {pop_statistic}")
plt.xlabel("")
plt.show()
plt.clf()

sample_stats = []
samp_size = 5
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    this_sample_stat = app_statistic(samp)
    sample_stats.append(this_sample_stat)

sns.histplot(sample_stats, stat = 'density')
plt.title(f"Sampling Dist of the {app_stat_text} \nMean: {round(np.mean(sample_stats),2)}")
plt.axvline(np.mean(sample_stats),color='r',linestyle='dashed')
plt.xlabel(f"Sample {app_stat_text}")
plt.show()
plt.clf()


#  calculating probabilities of sampling distributions
# Using the CLT, we first estimate that the mean weight of 10 randomly sampled salmon from this population is 
# normally distributed with mean = 60 and standard error = 40/10^.5. Then, we can use this probability distribution 
# to calculate the probability that 10 randomly sampled fish will have a mean weight less than or equal to 75.
x = 75
mean = 60
std_dev = 40
samp_size = 10
standard_error = std_dev / (samp_size**.5)
# remember that **.5 is raising to the power of one half, or taking the square root
 
stats.norm.cdf(x,mean,standard_error)






import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

## Setting up our parameters
std_dev = 20
samp_size = 25
standard_error = std_dev / (samp_size**.5)
#  cdf(x,mean,standard error)  x is the specific value your looking for.
cod_cdf = stats.norm.cdf(30,36, standard_error)
print(cod_cdf)
