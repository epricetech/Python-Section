# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 09:27:41 2023

@author: geron
"""

#  similiar to histo as they give a sense of central tendancy
#  the line in the center of box is the median
#  the edges of box are the q1 and q3 values.  the length of the box in the IQR
#  Whisters include most of the data and different ways to calculate
#  outliers are points that fall beyond the whiskers.  Represented with dots

#  first step is find meadian using the np.median() function
#  then find the edges q1 and q3

#  whiskers - display info related to the spread of the dataset
#  diffferent ways to plot whiskers - u can set them to min and max or a single standard deviation - most common is 1.5 times
# and if it cant meet that 1.5 it will go to the clostest point 
# the IQR from the 1st to 3rd quartile ex  q1 4  q3 9 = IQR 5  - whiskers is 5 * 1.5 = 7.5 units  so whiskers would extend
#  from -3.5 to 16.5


import numpy as np
from data import dataset

quartile_one = np.quantile(dataset, 0.25) 
quartile_three = np.quantile(dataset, 0.75)
# Define your variables here:
iqr = quartile_three - quartile_one
distance = iqr * 1.5
left_whisker = quartile_one - distance
right_whisker = quartile_three + distance

#Ignore the code below here
try:
  print("The interquartile range of the dataset is " + str(iqr) + ".")
except NameError:
  print("You haven't defined iqr.")
  
try:
  print("Each whisker should be " + str(distance) + " units away from the edges of the box.")
except NameError:
  print("You haven't defined distance.")
  
try:
  print("The left whisker should extend to " + str(left_whisker) + " .")
except NameError:
  print("You haven't defined left_whisker.")
  
try:
  print("The right whisker should extend to " + str(right_whisker) + " .")
except NameError:
  print("You haven't defined right_whisker.")


#outliers - point that falls outside the whiskers and shown as either a dot or astrisk


# b oxplot in matplot lib
import matplotlib.pyplot as plt
 
data = [1, 2, 3, 4, 5]
plt.boxplot(data)
plt.show()

#  2 boxplots side by side
import matplotlib.pyplot as plt
 
dataset_one = [1, 2, 3, 4, 5]
dataset_two = [3, 4, 5, 6, 7]
plt.boxplot([dataset_one, dataset_two])
plt.show()


import codecademylib3_seaborn
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)


a = np.random.normal(1, 1, 1000)
b = np.random.normal(0, 3, 1000)
c = np.random.normal(2, 1.5, 1000)
d = np.random.normal(-4, 5, 1000)
e = np.random.normal(5, 2, 1000)
plt.boxplot([a,b,c,d,e])
plt.show()
plt.subplot(511)
plt.hist(a)
plt.xlim([-20,20])
plt.subplot(512)
plt.hist(b)
plt.xlim([-20,20])
plt.subplot(513)
plt.hist(c)
plt.xlim([-20,20])
plt.subplot(514)
plt.hist(d)
plt.xlim([-20,20])
plt.subplot(515)
plt.hist(e)
plt.xlim([-20,20])
plt.tight_layout()
plt.show()
