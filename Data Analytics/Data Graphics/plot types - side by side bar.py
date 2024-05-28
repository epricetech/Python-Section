# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 08:40:33 2023

@author: geron
"""

# #In the graph above, there are 7 sets of bars, with 2 bars in each set. Each bar has a width of 0.8 
# (the default width for all bars in Matplotlib).

# If our first blue bar is at x=0, then we want the next blue bar to be at x=2, and the next to be at x=4, etc.
# Our first orange bar should be at x=0.8 (so that it is touching the blue bar), and the next orange bar should 
# be at x=2.8, etc.
# This is a lot of math, but we can make Python do it for us by copying and pasting this code:

# China Data (blue bars)
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 7 # Number of sets of bars
w = 0.8 # Width of each bar
x_values1 = [t*element + w*n for element
             in range(d)]


# That just generated the first set of x-values. To generate the second set, paste the code again, but change n to 2, 
# because this is the second dataset:

# US Data (orange bars)
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 7 # Number of sets of bars
w = 0.8 # Width of each bar
x_values2 = [t*element + w*n for element
             in range(d)]
Let’s examine our special code:
# this creates list comprehension which is a way of generating list from a formula and this code never really needs to change.
[t*element + w*n for element in range(d)]




#  creates a side by side bar chart
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

#Paste the x_values code here
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element
             in range(d)]

plt.bar(store1_x,sales1)

n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element
             in range(d)]
plt.bar(store2_x, sales2)

plt.show()






