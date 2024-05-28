# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:28:20 2023

@author: geron
"""
# Create a variable called lam that represents the rate parameter of our distribution.


# Stuck? Get a hint
# 2.
# You know that the rate parameter of a Poisson distribution is equal to the expected value. So in our factory, the rate parameter would equal the expected number of defects on a given day. You are curious about how often we might observe the exact expected number of defects.

# Calculate and print the probability of observing exactly lam defects on a given day.


# Stuck? Get a hint
# 3.
# Our boss said that having 4 or fewer defects on a given day is an exceptionally good day. You are curious about how often that might happen.

# Calculate and print the probability of having one of these days.


# Stuck? Get a hint
# 4.
# On the other hand, our boss said that having more than 9 defects on any given day is considered a bad day.

# Calculate and print the probability of having one of these bad days.


# Stuck? Get a hint
# Distribution in Practice
# 5.
# You’ve familiarized yourself a little bit about how the Poisson distribution works in theory by calculating different probabilities. But let’s look at what this might look like in practice.

# Create a variable called year_defects that has 365 random values from the Poisson distribution.


# Stuck? Get a hint
# 6.
# Let’s take a look at our new dataset. Print the first 20 values in this data set.


# Stuck? Get a hint
# 7.
# If we expect 7 defects on a given day, what is the total number of defects we would expect over 365 days?

# Calculate and print this value to the output terminal.


# Stuck? Get a hint
# 8.
# Calculate and print the total sum of the data set year_defects. How does this compare to the total number of defects we expected over 365 days?


# Stuck? Get a hint
# 9.
# Calculate and print the average number of defects per day from our simulated dataset.

# How does this compare to the expected average number of defects each day that we know from the given rate parameter of the Poisson distribution?


# Stuck? Get a hint
# 10.
# You’re worried about what the highest amount of defects in a single day might be because that would be a hectic day.

# Print the maximum value of year_defects.


# Stuck? Get a hint
# 11.
# Wow, it would probably be super busy if there were that many defects on a single day. Hopefully, it is a rare event!

# Calculate and print the probability of observing that maximum value or more from the Poisson(7) distribution.


# Stuck? Get a hint
# Extra
# 12.
# Congratulations! At this point, you have now explored the Poisson distribution and even worked with some simulated data. We have a couple of extra tasks if you would like an extra challenge. Feel free to try them out or move onto the next topic!

# Let’s say we want to know how many defects in a given day would put us in the 90th percentile of the Poisson(7) distribution. One way we could calculate this is by using the following method:

# stats.poisson.ppf(percentile, lambda) 
# percentile is equal to the desired percentile (a decimal between 0 and 1), and lambda is the lambda parameter of the Poisson distribution. This function is essentially the inverse of the CDF.

# Use this method to calculate and print the number of defects that would put us in the 90th percentile for a given day. In other words, on 90% of days, we will observe fewer defects than this number.


# Stuck? Get a hint
# 13.
# Now let’s see what proportion of our simulated dataset year_defects is greater than or equal to the number we calculated in the previous step.

# By definition of a percentile, we would expect 1 - .90, or about 10% of days to be in this range.

# To calculate this:

# Count the number of values in the dataset that are greater than or equal to the 90th percentile value.
# Divide this number by the length of the dataset.
# Click the hint if you want to see an example calculation.
import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: 
lam = 7
## Task 2:
lam_defects = stats.poisson.pmf(lam,lam)
print(lam_defects)
## Task 3:
print(stats.poisson.cdf(4,lam))
## Task 4:
print(stats.poisson.cdf(9,lam))

### Task Group 2 ###
## Task 5:
year_defects = stats.poisson.rvs(lam, size=365)
## Task 6:  prints the first 20 values
print(year_defects[0:20])
## Task 7:
print(lam*365)
## Task 8:
print(sum(year_defects))
## Task 9:
print(np.mean(year_defects))
print(year_defects.max())
## Task 11:
print(1 - stats.poisson.cdf(year_defects.max(), lam))

### Extra Bonus ###
# Task 12
print(stats.poisson.ppf(.9, lam))
# Task 13
count = sum(year_defects > stats.poisson.ppf(.9, lam)) / len(year_defects)
print(count)