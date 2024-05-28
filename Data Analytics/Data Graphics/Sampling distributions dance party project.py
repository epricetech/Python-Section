# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:10:11 2023

@author: geron
"""
# et’s investigate the helper functions we will use in the following sections. A file called helper_functions.py 
# should be opened in the workspace for you. It contains three functions: choose_statistic(), population_distribution(), 
# and sampling_distribution(). The code in these functions is similar to what we saw in the previous lesson, 
# but let’s explore these together.

# choose_statistic() allows us to choose a statistic we want to calculate for our sampling and population distributions. 
# It contains two parameters:

# x: An array of numbers
# sample_stat_text: A string that tells the function which statistic to calculate on x. 
# It takes on three values: “Mean”, “Minimum”, or “Variance”.
# population_distribution() allows us to plot the population distribution of a dataframe with one function call. 
# It takes the following parameter:

# population_data: the dataframe being passed into the function
# sampling_distribution() allows us to plot a simulated sampling distribution of a statistic. 
# The simulated sampling distribution is created by taking random samples of some size, calculating a particular statistic, 
# and plotting a histogram of those sample statistics. It contains three parameters:

# population_data: the dataframe being sampled from
# samp_size: the size of each sample
# stat: the specific statistic being measured for each sample — either “Mean”, “Minimum”, or “Variance”
# Read through these functions in helper_function.py to familiarize yourself with them. 
# Click the hint to see examples of population_distribution() and sampling_distribution() being used.

# Here is an example of how to use population_distribution():

# # example function use case
# population_distribution(population)
# Here is an example of how to use sampling_distribution():

# # example function use case for sampling distribution of the mean
# sampling_distribution(population, "Mean")



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import codecademylib3

def choose_statistic(x, sample_stat_text):
  # calculate mean if the text is "Mean"
  if sample_stat_text == "Mean":
    return np.mean(x)
  # calculate minimum if the text is "Minimum"
  elif sample_stat_text == "Minimum":
    return np.min(x)
  # calculate variance if the text is "Variance"
  elif sample_stat_text == "Variance":
      #Adding this ddof=1 parameter will divide our input by n-1 instead of n, therefore applying the sample variance formula.
      return np.var(x, ddof=1)
  # if you want to add an extra stat
  # raise error if sample_stat_text is not "Mean", "Minimum", or "Variance"
  else:
    raise Exception('Make sure to input "Mean", "Minimum", or "Variance"')

def population_distribution(population_data):
  # plot the population distribution
  sns.histplot(population_data, stat='density')
  # informative title for the distribution 
  plt.title(f"Population Distribution")
  # remove None label
  plt.xlabel('')
  plt.show()
  plt.clf()

def sampling_distribution(population_data, samp_size, stat):
  # list that will hold all the sample statistics
  sample_stats = []
  for i in range(500):
    # get a random sample from the population of size samp_size
    samp = np.random.choice(population_data, samp_size, replace = False)
    # calculate the chosen statistic (mean, minimum, or variance) of the sample
    sample_stat = choose_statistic(samp, stat)
    # add sample_stat to the sample_stats list
    sample_stats.append(sample_stat)
  
  pop_statistic = round(choose_statistic(population_data, stat),2)
  # plot the sampling distribution
  sns.histplot(sample_stats, stat='density')
  # informative title for the sampling distribution
  plt.title(f"Sampling Distribution of the {stat} \nMean of the Sample {stat}s: {round(np.mean(sample_stats), 2)} \n Population {stat}: {pop_statistic}")
  plt.axvline(pop_statistic,color='g',linestyle='dashed', label=f'Population {stat}')
  # plot the mean of the chosen sample statistic for the sampling distribution
  plt.axvline(np.mean(sample_stats),color='orange',linestyle='dashed', label=f'Mean of the Sample {stat}s')
  plt.legend()
  plt.show()
  plt.clf()
# functions that do specific things for the code below.  


from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import codecademylib3

# task 1: load in the spotify dataset
spotify_data = pd.read_csv('spotify_data.csv')
# task 2: preview the dataset
print(spotify_data.head(10))
# task 3: select the relevant column
song_tempos = spotify_data['tempo']
# task 5: plot the population distribution with the mean labeled
population_distribution(song_tempos)
# task 6: sampling distribution of the sample mean
sampling_distribution(song_tempos,30, 'Mean')
# task 8: sampling distribution of the sample minimum
sampling_distribution(song_tempos,30, 'Minimum')
# task 10: sampling distribution of the sample variance
sampling_distribution(song_tempos,30, 'Variance')
# task 13: calculate the population mean and standard deviation
population_mean = np.mean(song_tempos)
population_std = np.std(song_tempos)
# task 14: calculate the standard error
standard_error = population_std / (30**.5)
# task 15: calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs
print(stats.norm.cdf(140,population_mean, standard_error))
# task 16: calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs
print(1-stats.norm.cdf(150,population_mean,standard_error))
# EXTRA




