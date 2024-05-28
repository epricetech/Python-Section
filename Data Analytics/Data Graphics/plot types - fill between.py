# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:21:06 2023

@author: geron
"""

# fill between - uses plt.fill_between()  3 arugments  - must also use list comprehession
# y_lower = [i - 2 for i in y_values]    - subtracts 2 each time
#   y_upper = [i + 2 for i in y_values]   - adds 2 each time
# X-values - just like the x-values in plt.plot()
# Lower bound for y-values - sets the bottom of the shaded area
# Upper bound for y-values - sets the top of the shaded area
# Alpha - this will set the shading level between 0 and 1




x_values = range(10)
y_values = [10, 12, 13, 13, 15, 19, 20, 22, 23, 29]
y_lower = [8, 10, 11, 11, 13, 17, 18, 20, 21, 27]
y_upper = [12, 14, 15, 15, 17, 21, 22, 24, 25, 31]
 
plt.fill_between(x_values, y_lower, y_upper, alpha=0.2) #this is the shaded error
plt.plot(x_values, y_values) #this is the line itself
plt.show()





from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

#your work here
plt.plot(months,revenue)

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
y_lower = [i - (i * 0.1) for i in revenue]
y_upper = [i + (i * 0.1) for i in revenue]

plt.fill_between(months, y_lower, y_upper, alpha=0.2)
plt.show()
















