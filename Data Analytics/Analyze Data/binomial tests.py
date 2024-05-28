# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 08:53:40 2023

@author: geron
"""

# summarizing the sample

## sample size (number of rows): 
samp_size = len(candy)
 
## number with chocolate: 
total_with_chocolate = np.sum(candy.chocolate == 'yes')


# This creates the summary of the sample.  gets the sample size and what specific aspect we are looking for.  
import numpy as np
import pandas as pd
import codecademylib3

monthly_report = pd.read_csv('monthly_report.csv')

#print the head of monthly_report:
print(monthly_report.head(5))

#calculate and print sample_size:
sample_size = len(monthly_report)
print(sample_size)

#calculate and print num_purchased:
num_purchased = np.sum(monthly_report.purchase == 'y')
print(num_purchased)



#  simulating randomness

flip = np.random.choice(['heads', 'tails'], size=1, p=[0.5, 0.5])
print(flip) 
## output is either ['heads'] or ['tails']


flip = np.random.choice(['heads', 'tails'], size=10, p=[0.5, 0.5])
print(flip)
## output is something like: ['heads' 'heads' 'heads' 'tails' 'tails' 'heads' 'heads' 'tails' 'heads' 'heads']



import numpy as np
import pandas as pd

monthly_report = pd.read_csv('monthly_report.csv')
#  not totally sure why the .9.  I think it is because these variables can only be between -1 and 1
#simulate one visitor:
one_visitor = np.random.choice(['y', 'n'], size=1, p=[0.1,0.9])
print(one_visitor)
#simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[.1,.9])
print(simulated_monthly_visitors)



# Simulating the null distribution - first part of running a hypothesis test is to form a null hypothesis.  null value here
# would be 50% of 5 heads in 10 flips but that doesnt always happen
#this is just seeing how many times a certain value shoes up in the sample size randomly
flips = np.random.choice(['heads', 'tails'], size=10, p=[0.5, 0.5])
num_heads = np.sum(flips == 'heads')
print(num_heads)
## output: 4

#  same type of thing as above
import numpy as np
import pandas as pd

monthly_report = pd.read_csv('monthly_report.csv')

#simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

#calculate the number of simulated visitors who made a purchase:
num_purchased = np.sum(simulated_monthly_visitors == 'y')
print(num_purchased)


# In this code chunk, we’ve done the following:

# initialized an empty list named outcomes to store the number of ‘heads’ from simulated samples of coin flips
# set up a for-loop to repeat the steps below 10000 times:
# flip a fair coin 10 times
# calculate the number of those 10 flips that came up heads
# append that number onto outcomes


outcomes = []
for i in range(10000): 
    flips = np.random.choice(['heads', 'tails'], size=10, p=[0.5, 0.5])
    num_heads = np.sum(flips == 'heads')
    outcomes.append(num_heads)
print(outcomes)
## output is something like: [3, 4, 5, 8, 5, 6, 4, 5, 3, 2, 8, 5, 7, 4, 4, 5, 4, 3, 6, 5,...]
#  find the min and max of the results of the 10000 tests
min_heads = np.min(outcomes) 
print(min_heads) #output: 0
 
max_heads = np.max(outcomes)
print(max_heads) #output: 10

#  another example
import numpy as np
import pandas as pd

null_outcomes = []

#start for loop here:
for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'],   size=500, p=[0.1, 0.9])
  

  num_purchased = np.sum(simulated_monthly_visitors == 'y')
  null_outcomes.append(num_purchased)
print(null_outcomes)


#calculate the minimum and maximum values in null_outcomes here:
null_min = np.min(null_outcomes)
null_max = np.max(null_outcomes)
print(null_min)
print(null_max)


# inspecting the null distribution with histogram
# We can plot a histogram of outcomes using matplotlib.pyplot.hist(). 
# We can also add a vertical line at any x-value using matplotlib.pyplot.axvline():

import matplotlib.pyplot as plt
plt.hist(outcomes)
plt.axvline(2, color = 'r')
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import codecademylib3

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#plot the histogram here:
plt.hist(null_outcomes)
plt.axvline(41, color='r')

plt.show()



#  confidence intervals using the np.percentile() function
#  the idea is we say we are a certain percentage confident in our probability because that % of results of tests were in a 
#   specific range.  Like 100 visitors and we expect 90% to show.  But our tests show it can range from 50 to 100 but 95% of
#  the test results were around 90% so our confidence is we are 95% certain 90% will show up

np.percentile(outcomes, [2.5,97.5])
# output: [37. 63.]
# We calculated the 2.5th and 97.5th percentiles so that exactly 5% of the data falls outside those percentiles 
# (2.5% above the 97.5th percentile, and 2.5% below the 2.5th percentile). 
# This leaves us with a range covering 95% of the data.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import codecademylib3

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the 90% interval here:  This is the 5th and 95 percentile
null_90CI = np.percentile(null_outcomes, [5,95])
print(null_90CI)



#  calculating a one-sided p-value  - depend on the alternative hypothesis of a test, a description of the differnece
#  from the expecteation.  the result is the one-sided p-value
#  example of seeing what the probability of seeing 2 or less heads in 10 flips - our null hypothesis is 5 or 50%
import numpy as np
outcomes = np.array(outcomes)
p_value = np.sum(outcomes <= 2)/len(outcomes) 
print(p_value) #output: 0.059  -  this is referred to as a one-sided p value

import numpy as np
import pandas as pd

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the p-value here:
null_outcomes = np.array(null_outcomes)
p_value = np.sum(null_outcomes <= 41)/len(null_outcomes)
print(p_value)
#output is around 0.1


# Calculating a two-sided p-value - defualt function setting for python
#  this doesnt focus on being  less than 2 like example before.  It looks for all results who are 
#  if 10 flips the null hypothisis is 5 so this code is checking for values that are 3 away from 5.  
#  the | also or works for comparing multiple values at once
outcomes = np.array(outcomes)
p_value = np.sum((outcomes <= 2) | (outcomes >= 8))/len(outcomes)
print(p_value) #output: 0.12


import numpy as np
import pandas as pd

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the p-value here:
null_outcomes = np.array(null_outcomes)
p_value = np.sum((null_outcomes <= 41) | (null_outcomes >= 59))/len(null_outcomes)
print(p_value)
#  output is 0.2109

