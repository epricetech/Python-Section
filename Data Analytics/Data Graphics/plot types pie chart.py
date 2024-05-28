# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:51:20 2023

@author: geron
"""

#  pie charts use the plt.pie() function   - use plt.axis('equal') to untilt the pie chart


from matplotlib import pyplot as plt
import numpy as np

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#make your pie chart here
plt.pie(payment_method_freqs)
plt.axis('equal')

plt.show()


#  putting legend and lables on pie chart

budget_data = [500, 1000, 750, 300, 100]
budget_categories = ['marketing', 'payroll', 'engineering', 'design', 'misc']
 
plt.pie(budget_data)
plt.legend(budget_categories)
#  or this code to do the same thing
plt.pie(budget_data, labels=budget_categories)


#  using autopct argument in plt.pie  to set percentages.
#  some examples
# '%0.2f' — 2 decimal places, like 4.08
# '%0.2f%%' — 2 decimal places, but with a percent sign at the end, like 4.08%. You need two 
# consecutive percent signs because the first one acts as an escape character, so that the second one
#  gets displayed on the chart.
# '%d%%' — rounded to the nearest int and with a percent sign at the end, like 4%.

plt.pie(budget_data,
        labels=budget_categories,
        autopct='%0.1f%%')


from matplotlib import pyplot as plt

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, autopct='%0.1f%%')
plt.axis('equal')
plt.legend(payment_method_names)


plt.show()
















