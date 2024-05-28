# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:09:10 2023

@author: geron
"""

#  plt.hist() function.  Can also add bins argument which will set the distance between the min and max value of each bin
#  a bin is a group of numbers all the same length.  like looking for numbers between 0 and 10 and 20 an 20  each on is a bin



import codecademylib
from matplotlib import pyplot as plt
from script import sales_times

#create the histogram here
plt.hist(sales_times, bins=20)
plt.show()


#  multiple hisograms - when we want to compare 2 different distibutions.  use the keyword alpha for shading


plt.hist(a, range=(55, 75), bins=20, alpha=0.5)
plt.hist(b, range=(55, 75), bins=20, alpha=0.5)


# the histtype step will just dawy and outline of histogram
plt.hist(a, range=(55, 75), bins=20, histtype='step')
plt.hist(b, range=(55, 75), bins=20, histtype='step')

# Another problem we face is that our histograms might have different numbers of samples, making one much bigger than the other.
#  We can see how this makes it difficult to compare qualitatively, by adding a dataset b with a much bigger size value:

a = normal(loc=64, scale=2, size=10000)
b = normal(loc=70, scale=2, size=100000)
 
plt.hist(a, range=(55, 75), bins=20)
plt.hist(b, range=(55, 75), bins=20)
plt.show()


#  to solve the above issue we can normalize the histo by using density=True  command divides the height of each column by 
#  a constant such that the total shaded area of the histo sumes to 1

a = normal(loc=64, scale=2, size=10000)
b = normal(loc=70, scale=2, size=100000)
 
plt.hist(a, range=(55, 75), bins=20, alpha=0.5, density=True)
plt.hist(b, range=(55, 75), bins=20, alpha=0.5, density=True)
plt.show()




import codecademylib3
from matplotlib import pyplot as plt
from script import sales_times1
from script import sales_times2

plt.hist(sales_times1, bins=20, alpha=0.4, density=True)
#plot your other histogram here
plt.hist(sales_times2, alpha=0.4,density=True)


plt.show()










