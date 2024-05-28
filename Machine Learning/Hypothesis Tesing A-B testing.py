# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:17:47 2023

@author: geron
"""

#  A/B testing between 2 options.  where outcome of interest is categorical an a/b test is conducted using a 
#  Chi-square test.  To determine sample size you need 3 numbers
#  1.  Baseline conversion rate
#  2.  Minimum detectable effect - also called minimum desired life
#  3.  Statistical significance threshold

#  Baseline Conversion rate - calculate by looking at historical data for the option that we are currently using.  It is the
#  extimate for the percentage of desired results.  Example the baseline would be for the following.  Sample size of 2000 people
#  find that 320 of those people bought t-shirts so 
baseline = 320/2000*100
print(baseline)

number_of_site_visitors = 2000.0
number_of_converted_visitors = 1300.0

# calculate baseline_rate and print it out:

baseline_rate = number_of_converted_visitors/number_of_site_visitors*100
print(baseline_rate)


#  Minimum Detectable Effect
#  in order to detect precise differences we need a very large sample size.  in order to get right sample size we need to know
#  the smalles difference that we actually care to measure.  This smallest difference is our minimum detectable effect
#  #  generally expressed as a percent of the baseline conversion rate.  
#  Example we have 6% currrent subscribers if we change layout we need at least 8% subscribers go to the new one to make it worth it
baseline = 6
new = 8
min_detectable_effect = (new - baseline) / baseline * 100
print(min_detectable_effect) #output: 33.0 - minimum detectable rate

baseline = 8
new = 12

mde = (new-baseline)/ baseline*100
print(mde)   #  output is 50.0


# Significance Threshold  -  this is just like the p-value threshold.  Common is 0.05 and a false negative rate of 20%
# and also false positve results


# Here are two important rules for making sure that A/B tests remain unbiased:

# Don’t continue to run the test after the predetermined sample size, until “significant” results are found.
# Don’t stop a test before reaching the predetermined sample size, just because your results reach significance early 
# (unless there are ethical reasons that require you to stop, like a prescription drug trial).

# calculate baseline:
baseline = 10
print("baseline: ", baseline)

# calculate MDE:
MDE = (14 - 10)/10 * 100
print("Minimum Detectable Effect: ", MDE)

# calculate significance threshold:
sig_threshold = 5
print("significance threshold: ", sig_threshold)

# calculate total sample size: 
samp_size= 	2060
print("sample size: ", samp_size)
