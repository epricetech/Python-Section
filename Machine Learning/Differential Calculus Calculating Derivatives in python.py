# -*- coding: utf-8 -*-
"""
Created on Tue May  9 08:58:08 2023

@author: geron
"""

##  f(x) = x^2 + 3  - function
#The pow() function within the f(x) function we defined allows us to calculate the values of x2, and we use a list 
#comprehension to create a list of the y-values in a variable called f_array_y.


from math import pow
# dx is the "step" between each x value
dx = 0.05
def f(x):
  # to calculate the y values of the function
  return pow(x, 2) + 3
# x values
f_array_x = [x for x in np.arange(0,4,dx)]
# y values
f_array_y = [f(x) for x in np.arange(0,4,dx)]


##To compute the derivative of f_array, we use a NumPy function called gradient()
#gradient() takes in an array (in this case, a one-dimensional array) as its first argument. 
#We also need to specify the distance between the x values, which is dx
f_array_deriv = np.gradient(f_array_y, dx)




# Turning our function into an array 
import numpy as np
from math import sin
import codecademylib3
import matplotlib.pyplot as plt

# our change in x value
dx = 1
def f(x):
    return sin(x) 
sin_x = [x for x in np.arange(0,20,dx)]
sin_y = [f(x) for x in np.arange(0,20,dx)]
sin_deriv = np.gradient(sin_y,dx)
plt.plot(sin_x, sin_y)
plt.plot(sin_x, sin_deriv)
plt.show()

