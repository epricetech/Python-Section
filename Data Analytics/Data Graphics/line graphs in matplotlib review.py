# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:44:02 2023

@author: geron
"""



from matplotlib import pyplot as plt

x = [2,4,6,8,10,12,14,16,18,20]
y1 = [1,2,3,4,5,6,7,8,9,10]
y2 = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]

plt.plot(x, y1, marker='o', color='pink')
plt.plot(x, y2, marker='o', color='gray')

plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')

plt.legend('The Axis', loc=4)


plt.show()








