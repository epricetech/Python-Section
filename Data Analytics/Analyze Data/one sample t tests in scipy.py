# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 13:26:58 2023

@author: geron
"""

#  used for comparing a sample average toa hypothetical population average.  from scipy.stats. import ttest_1samp is need
# to be used for the one sample t test.  Then to use
#  Syntax
#  tstat, pval = ttest_1samp(sample_distibution, expected_mean)
#  Sample disctibution is the sample size and expected_mean is our null hypothoisis and are alternative hypothisis is is not 

# As a final exercise, some data has been loaded for you with purchase prices for consecutive days at BuyPie.
#  You can access the first day using daily_prices[0], the second using daily_prices[1], etc.. 
#  To practice running a one-sample t-test and inspecting the resulting p-value, try the following:

# Calculate and print out a p-value for day 1 where the null hypothesis is that the average purchase price was 1000 Rupees 
# and the alternative hypothesis is that the average purchase price was not 1000 Rupees. Print out the p-value.

# Run the same hypothesis tests for days 1-10 (the fastest way to do this is with a for-loop!) and print 
# out the resulting p-values. What’s the smallest p-value you observe for those 10 days?

# Try changing the null hypothesis so that the expected population mean that you’re testing against is 
# different from 1000. Try any numbers that you want. How do your p-values change?
from scipy.stats import ttest_1samp
import numpy as np

daily_prices = np.genfromtxt("daily_prices.csv", delimiter=",")

# day 1:
tstat, pval = ttest_1samp(daily_prices[0], 1000)
print("day 1 p-value:")
print(pval)

# 10 days:
for i in range(10):
  tstat, pval = ttest_1samp(daily_prices[i], 1000)
  print("day",i+1, "p-value:")
  print(pval)

# 10 days with a different null hypothesis
print("day 1-10 with a different alternative hypothesis:")
for i in range(10):
  tstat, pval = ttest_1samp(daily_prices[i], 950)
  print("day",i+1, "p-value:")
  print(pval)


# Output:
# day 1 p-value:
# 0.6071186852381734
# day 1 p-value:
# 0.6071186852381734
# day 2 p-value:
# 0.4093623236367092
# day 3 p-value:
# 0.6823152912621231
# day 4 p-value:
# 0.9396281562313855
# day 5 p-value:
# 0.8434532443692766
# day 6 p-value:
# 0.018765443076610062
# day 7 p-value:
# 0.6240646986588566
# day 8 p-value:
# 0.8594296361029083
# day 9 p-value:
# 0.774383958509746
# day 10 p-value:
# 0.6813407662727201
# day 1-10 with a different alternative hypothesis:
# day 1 p-value:
# 0.006068400953830715
# day 2 p-value:
# 0.00248388684038805
# day 3 p-value:
# 0.00576062384123009
# day 4 p-value:
# 0.02286083709081289
# day 5 p-value:
# 0.02269727235522927
# day 6 p-value:
# 3.729171844379401e-06
# day 7 p-value:
# 0.007970863097214977
# day 8 p-value:
# 0.05444296471985292
# day 9 p-value:
# 0.022347610165122662
# day 10 p-value:
# 0.07949349326248725