# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 08:23:53 2023

@author: geron
"""

#  uses plt.bar function with 2 arguments to compare data.

heights = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
x_values = range(len(heights))

days_in_year = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
plt.bar(range(len(days_in_year)),
        days_in_year)
plt.show()



from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(sales)),sales)
plt.show()



# can also set ticks like in line graphs
# Create an axes object
# ax = plt.subplot()

# Set the x-tick positions using a list of numbers
# ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])

# Set the x-tick labels using a list of strings
# ax.set_xticklabels(['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'])

# If your labels are particularly long, you can use the rotation keyword to rotate your labels by a specified number of degrees:
# ax.set_xticklabels(['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'],
# rotation=30)


from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

#create your ax object here
ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)


plt.show()




