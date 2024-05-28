# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:09:57 2023

@author: geron
"""

#  stacked bars - when you want to compare but keep total relationship.  keyword is bottom
# the first set of bars is plotted normally:

video_game_hours = [1, 2, 2, 1, 2]
 
plt.bar(range(len(video_game_hours)),
  video_game_hours) 
# and the second set of bars has bottom specified:

book_hours = [2, 3, 4, 2, 1]
 
plt.bar(range(len(book_hours)),
  book_hours,
  bottom=video_game_hours)




from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

plt.bar(range(len(drinks)),sales1)
plt.bar(range(len(drinks)),sales2, bottom=sales1)

plt.legend(['Location 1', 'Location 2'])

plt.show()





