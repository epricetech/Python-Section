# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:18:28 2023

@author: geron
"""

#  error bars used to show deviations - add argument yerr=# to plt.bar() function.  Can also change capsize by adding
#  the capsize=# argument as well.  

values = [10, 13, 11, 15, 20]
yerr = 2
plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
plt.show()



from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# Plot the bar graph here
plt.bar(range(len(drinks)), ounces_of_milk, yerr=error,capsize=5)

plt.show()



