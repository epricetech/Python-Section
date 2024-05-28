# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:45:17 2023

@author: geron
"""


# his code does the following:

# Set the significance threshold equal to 0.05 and a counter for false positives equal to zero.
# Repeat these steps 1000 times:
# Simulate 100 learners, where each learner has a 70% chance of answering a quiz question correctly.
# Calculate the number of simulated learners who answered the question correctly. Note that, because each 
# learner has a 70% chance of answering correctly, this number will likely be around 70, but will vary e
# very time by random chance.
# Run a binomial test for the simulated sample where the null hypothesis is that the probability of a 
# correct answer is 70% (0.7). Note that, every time we run this test, the null hypothesis is true 
# because we simulated our data so that the probability of a correct answer is 70%.
# Add 1 to our false positives counter every time we make a type I error (the p-value is significant).
# Print the proportion of our 1000 tests (on simulated samples) that resulted in a false positive.
# Note that the proportion of false positive tests is very similar to the value of the significance threshold (0.05).



false_positives = 0
sig_threshold = 0.05
 
for i in range(1000):
    sim_sample = np.random.choice(['correct', 'incorrect'], size=100, p=[0.7, 0.3])
    num_correct = np.sum(sim_sample == 'correct')
    p_val = binom_test(num_correct, 100, 0.7)
    if p_val < sig_threshold:
        false_positives += 1
 
print(false_positives/1000) #Output: 0.0512


import codecademylib3

# Import libraries
import numpy as np
from scipy.stats import binom_test

# Initialize num_errors
false_positives = 0
# Set significance threshold value
sig_threshold = 0.01

# Run binomial tests & record errors
for i in range(1000):
    sim_sample = np.random.choice(['correct', 'incorrect'], size=100, p=[0.8, 0.2])
    num_correct = np.sum(sim_sample == 'correct')
    p_val = binom_test(num_correct, 100, .8)
    if p_val < sig_threshold:
        false_positives += 1

# Print proportion of type I errors 
print(false_positives/1000)
# output
# 0.012

















