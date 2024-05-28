# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 08:00:02 2023

@author: geron
"""


# The full dataset has been loaded for you as heart, then split into two subsets:

# yes_hd, which contains data for patients with heart disease
# no_hd, which contains data for patients without heart disease
# For this project, we’ll investigate the following variables:

# chol: serum cholestorol in mg/dl
# fbs: An indicator for whether fasting blood sugar is greater than 120 mg/dl (1 = true; 0 = false)
# To start, we’ll investigate cholesterol levels for patients with heart disease. Use the dataset yes_hd to save 
# cholesterol levels for patients with heart disease as a variable named chol_hd.


# Hint
# Fill in the following code:

# chol_hd = yes_hd.___
# 2.
# In general, total cholesterol over 240 mg/dl is considered “high” (and therefore unhealthy). 
# Calculate the mean cholesterol level for patients who were diagnosed with heart disease and print it out. 
# Is it higher than 240 mg/dl?


# Hint
# Use np.mean to calculate the mean of chol_hd (created in the previous step).

# 3.
# Do people with heart disease have high cholesterol levels (greater than or equal to 240 mg/dl) on average? 
# Import the function from scipy.stats that you can use to test the following null and alternative hypotheses:

# Null: People with heart disease have an average cholesterol level equal to 240 mg/dl
# Alternative: People with heart disease have an average cholesterol level that is greater than 240 mg/dl
# Note: Unfortunately, the scipy.stats function we’ve been using does not (at the time of writing) 
# have an alternative parameter to change the alternative hypothesis for this test. 
# Therefore, you’ll have to run a two-sided test. However, since you calculated earlier that the 
# average cholesterol level for heart disease patients is greater than 240 mg/dl, you can calculate the 
# p-value for the one-sided test indicated above simply by dividing the two-sided p-value in half.


# Hint
# For this test, we need a one-sample t-test. To import the function:

# from scipy.stats import ttest_1samp
# 4.
# Run the hypothesis test indicated in task 3 and print out the p-value. Can you conclude that 
# heart disease patients have an average cholesterol level significantly greater than 240 mg/dl? 
# Use a significance threshold of 0.05.


# Hint
# ttest_1samp has two inputs: the sample of values (in this case, the cholesterol levels for patients with heart disease) 
# and the null value (in this case, 240). It has two outputs, the t-statstic and a p-value.

# When you divide the p-value by two (in order to run the one-sided test), you should get a p-value of 0.0035. 
# This is less than 0.05, suggesting that heart disease patients have an average cholesterol level significantly 
# higher than 240 mg/dl.

# 5.
# Repeat steps 1-4 in order to run the same hypothesis test, but for patients in the sample who were not 
# diagnosed with heart disease. Do patients without heart disease have average cholesterol levels significantly 
# above 240 mg/dl?


# Hint
# The syntax should be almost identical, but use the no_hd dataset instead of yes_hd.

# Fasting Blood Sugar Analysis
# 6.
# Let’s now return to the full dataset (saved as heart). How many patients are there in this dataset? 
# Save the number of patients as num_patients and print it out.


# Hint
# Use the len() function to calculate the number of rows in heart.

# 7.
# Remember that the fbs column of this dataset indicates whether or not a patient’s fasting blood sugar 
# was greater than 120 mg/dl (1 means that their fasting blood sugar was greater than 120 mg/dl; 0 means 
#                             it was less than or equal to 120 mg/dl).

# Calculate the number of patients with fasting blood sugar greater than 120. Save this number as num_highfbs_patients 
# and print it out.


# Hint
# Since patients have a value of 1 in the fbs column if their fasting blood sugar is greater than 120 mg/dl, and 0 otherwise,
#  you can simply add up all the numbers in the fbs column of heart using np.sum().

# 8.
# Sometimes, part of an analysis will involve comparing a sample to known population values to see if the sample appears
#  to be representative of the general population.

# By some estimates, about 8% of the U.S. population had diabetes (diagnosed or undiagnosed) in 1988 when this data
#  was collected. While there are multiple tests that contribute to a diabetes diagnosis, fasting blood sugar levels
#  greater than 120 mg/dl can be indicative of diabetes (or at least, pre-diabetes). If this sample were representative
#  of the population, approximately how many people would you expect to have diabetes? Calculate and print out this number.

# Is this value similar to the number of patients with a resting blood sugar above 120 mg/dl — or different?


# Hint
# We want to calculate 8% of the sample size (which is 303). Therefore, we should multiply 0.08*303.
#  This comes out to approximately 24 patients, which is almost half the number with fbs > 120 in the sample (45).

# 9.
# Does this sample come from a population in which the rate of fbs > 120 mg/dl is equal to 8%? Import the 
# function from scipy.stats that you can use to test the following null and alternative hypotheses:

# Null: This sample was drawn from a population where 8% of people have fasting blood sugar > 120 mg/dl
# Alternative: This sample was drawn from a population where more than 8% of people have fasting blood sugar > 120 mg/dl

# Hint
# This hypothesis test requires a binomial test. We can import the function for a binomial test as follows:

# from scipy.stats import binom_test
# 10.
# Run the hypothesis test indicated in task 9 and print out the p-value. Using a significance threshold of 0.05, 
# can you conclude that this sample was drawn from a population where the rate of fasting blood sugar > 120 mg/dl is 
# significantly greater than 8%?


# Hint
# The binom_test() function takes four parameters (in order):

# The observed number of “successes” (in this case, the number of people in the sample who had fasting blood 
#                                     sugar greater than 120 mg/dl)

# The number of “trials” (in this case, the number of patients)

# The null probability of “success” (in this case, 0.08)

# The alternative parameter, which indicates the alternative hypothesis for the test (eg.,'two-sided' 'greater' or 'less')

# The output is the p-value.

# If you run the test correctly, you should get a p-value of 4.689471951449078e-05 which is 
# equivalent to 0.0000469 (the e-5 at the end indicates scientific notation). This is less than 0.05, 
# indicating that this sample likely comes from a population where more than 8% of people have fbs > 120 mg/dl.


# import libraries
import codecademylib3
import pandas as pd
import numpy as np

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# get cholesterol levels for patients with heart disease
chol_hd = yes_hd.chol

# calculate mean cholesterol level for patients with hd
print(np.mean(chol_hd))

# compare to cut-off for high cholesterol
from scipy.stats import ttest_1samp
tstat, pval = ttest_1samp(chol_hd, 240)
print(pval/2)

# get cholesterol levels for patients without heart disease
chol_no_hd = no_hd.chol

# calculate mean cholesterol level for patients w/o hd
print(np.mean(chol_no_hd))

# compare to cut-off for high cholesterol
from scipy.stats import ttest_1samp
tstat, pval = ttest_1samp(chol_no_hd, 240)
print(pval/2)

# calculate number of patients total
num_patients = len(heart)
print(num_patients)

# calculate number of patients with fbs>120
num_highfbs_patients = np.sum(heart.fbs)
print(num_highfbs_patients)

# calculate 8% of sample size
print(0.08*num_patients)

# run binomial test
from scipy.stats import binom_test
pval = binom_test(num_highfbs_patients, num_patients, .08, alternative='greater')
print(pval)

#output  4.689471951449078e-05





