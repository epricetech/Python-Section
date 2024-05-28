# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:59:56 2023

@author: geron
"""

# with small sample size you get variance in the mean from each sample.  To address you can plot a histogram of all the 
# sample means.  That will provide a sampling distibution

salmon_population = population['Salmon_Weight']
 
sample_size = 50
sample_means = []
 
# loop 500 times to get 500 random sample means
for i in range(500):
  # take a sample from the data:
  samp = np.random.choice(salmon_population, sample_size, replace = False)
  # calculate the mean of this sample:
  this_sample_mean = np.mean(samp)
  # append this sample mean to a list of sample means
  sample_means.append(this_sample_mean)
 
# plot all the sample means to show the sampling distribution
sns.histplot(sample_means, stat='density')
plt.title("Sampling Distribution of the Mean")
plt.show()