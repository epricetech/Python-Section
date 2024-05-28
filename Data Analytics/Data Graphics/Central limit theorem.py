# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 09:56:14 2023

@author: geron
"""

#  this is used to speciffically describe the sampling distributions of the mean. and only applys to the mean and nothing else

# In order to see the Central Limit Theorem in action, let’s look at another population of fish that is not normally distributed.

# We have loaded this data on the weight of cod fish into the workspace.

# Uncomment the three lines underneath ## Checkpoint 1 to see the plot of the distribution of cod fish. Note the distribution.

# Checkpoint 2 Passed

# Hint
# Make sure these lines are uncommented:

# plt.hist(population, bins=50, density=True)
# plt.title("Population Distribution")
# plt.show()
# The distribution is not normal (which would look like a bell curve). It is highly skewed right.

# 2.
# Now that we have seen the skewed population distribution, let’s simulate a sampling distribution of the mean.
# According to the CLT, we will see a normal distribution once the sampling size is large enough. 
# To start, we have set the sample size to 6.

# Uncomment the five lines at the very bottom, run the code once, and take a look at the sampling distribution.

# Remember to scroll down to see the second plot.

# Checkpoint 3 Passed

# Hint
# With such a small sample size, the sampling distribution looks slightly skewed. 
# This is because the population was not normally distributed and we have a small sample size.

# 3.
# Now change the sample size to 50 and run the code. Does the estimated sampling distribution look more normal now?

# Checkpoint 4 Passed

# Hint
# Change the variable named samp_size to 50. Now that we have increased the sample size, 
# the sampling distribution should look more normal.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import codecademylib3

cod_population = pd.read_csv("cod_population.csv")
# Save transaction times to a separate numpy array
population = cod_population['Cod_Weight']

## Checkpoint 1:
sns.histplot(population, stat = 'density' )
plt.title("Population Distribution")
plt.show()

sample_means = []

# Below is our sample size
samp_size = 50

for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    this_sample_mean = np.mean(samp)
    sample_means.append(this_sample_mean)

## Checkpoint 2
plt.clf() # this closes the previous plot
sns.histplot(sample_means, stat = 'density' )
plt.title("Sampling Distribution of the Mean")
plt.xlabel("Weight (lbs)")
plt.show()





# In the workspace, we’ve set up a simulation of a population that has a mean of 10 and a standard deviation of 10. 
# We’ve set a sample size of 50.

# According to the CLT, we should have a sampling distribution of the mean that is normally distributed and has a mean 
# that is close to the population mean.

# Run the code once. Does what you see align with the CLT?

# Make sure to scroll down in the web browser to see the sampling distribution of the mean.

# Checkpoint 2 Passed

# Hint
# Yes, what we are seeing aligns with the CLT. The sampling distribution of the mean looks like a bell curve 
# and has a mean close to the population mean.

# 2.
# Set variable samp_size equal to 6 and run the code.

# Why do you think the CLT applies here, even with a smaller sample size?

# Checkpoint 3 Passed

# Hint
# Because the original population is normally distributed, the CLT applies even with a smaller sample size.


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import codecademylib3

# Set the population mean & standard deviation:
population_mean = 10
population_std_dev = 10
# Set the sample size:
samp_size = 6

# Create the population
population = np.random.normal(population_mean, population_std_dev, size = 100000)

# Simulate the samples and calculate the sampling distribution
sample_means = []
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    sample_means.append(np.mean(samp))

mean_sampling_distribution = round(np.mean(sample_means),3)

# Plot the original population
sns.histplot(population, stat = 'density')
plt.title(f"Population Mean: {population_mean} ")
plt.xlabel("")
plt.show()
plt.clf()

## Plot the sampling distribution
sns.histplot(sample_means, stat='density')
# calculate the mean and SE for the probability distribution
mu = np.mean(population)
sigma = np.std(population)/(samp_size**.5)
# plot the normal distribution with mu=popmean, sd=sd(pop)/sqrt(samp_size) on top
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

plt.plot(x, stats.norm.pdf(x, mu, sigma), color='k', label = 'normal PDF')
plt.title(f"Sampling Dist Mean: {mean_sampling_distribution}")
plt.xlabel("")
plt.show()



# Standard Error

# In the workspace, you can see a population distribution and a sampling distribution 
# (scroll down to see the sampling distribution). Right now, the sample size is set to 10.

# Increase the sample size to 50 and note the change in the shape of the sampling distribution.

# A smaller standard error means that the distribution will be taller & skinnier. Is that the case?

# Remember to scroll down to see the 2nd plot after you hit run.

# Checkpoint 2 Passed

# Stuck? Get a hint
# 2.
# Now increase the standard deviation of the population to 30.

# This means that the population distribution will have more variation (and will therefore appear wider and flatter). 
# The sampling distribution will also become wider and flatter because the standard error will increase (due to the larger numerator).

# Does what you see line up with what you expect?

# Checkpoint 3 Passed

# Stuck? Get a hint
# 3.
# Play around with the two variables samp_size and population_std_dev some more.

# Keep in mind that:

# As sample size increases, the standard error will decrease.
# As the population standard deviation increases, so will the standard error.


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import codecademylib3

population_mean = 36
population_std_dev = 30
# Set the sample size:
samp_size = 50

### Below is code to create simulated dataset and calculate Standard Error

# Create the population
population = np.random.normal(population_mean, population_std_dev, size = 100000)

## Simulate the sampling distribution
sample_means = []
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    sample_means.append(np.mean(samp))

mean_sampling_distribution = round(np.mean(sample_means),3)
std_sampling_distribution = round(np.std(sample_means),3)

std_error = population_std_dev / (samp_size **0.5)

sns.histplot(population, stat = 'density')
plt.title(f"Population Mean: {population_mean} \n Population Std Dev: {population_std_dev} \n Standard Error = {population_std_dev} / sq rt({samp_size}) \n Standard Error = {std_error} ")
plt.xlim(-50,125)
plt.ylim(0,0.045)
plt.show()
plt.clf()

## Plot the sampling distribution
sns.histplot(sample_means, stat = 'density')
# calculate the mean and SE for the probability distribution
mu = np.mean(population)
sigma = np.std(population)/(samp_size**.5)

# plot the normal distribution with mu=popmean, sd=sd(pop)/sqrt(samp_size) on top
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma), color='k', label = 'normal PDF')
# plt.axvline(mean_sampling_distribution,color='r',linestyle='dashed')
plt.title(f"Sampling Dist Mean: {mean_sampling_distribution} \n Sampling Dist Standard Deviation: {std_sampling_distribution}")
plt.xlim(20,50)
plt.ylim(0,0.3)
plt.show()

