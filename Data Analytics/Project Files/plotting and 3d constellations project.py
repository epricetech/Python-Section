# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:18:14 2023

@author: geron
"""

# Import internal library
import codecademylib3

# 1
# Import libraries and modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# Import 3D visualization library
from mpl_toolkits.mplot3d import Axes3d

# 2
# View given x,y,z coordinates
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]

# 3
# Create a figure
fig = plt.figure()
# Add your subplot
ax = fig.add_subplot(1,1,1)

# Create a scatter plot
plt.scatter(x,y)
plt.show()

# 4
# Create a figure
fig_3d = plt.figure()
# Add your subplot
ax_3d = fig_3d.add_subplot(1,1,1, projection='3d')

# Create a scatter plot
plt.scatter(x,y,z)
plt.show()

# Challenge
# Create a night sky scatter plot
# Create a figure
fig = plt.figure()
# Add your subplot
ax = fig.add_subplot(1,1,1)
# Change color of plot background
ax.set_facecolor((0.0,0.0,0.0))

# Create a scatter plot with black background
ax.scatter(x,y,color=(1.0,1.0,1.90))
plt.show()
# Create a figure
fig = plt.figure()
# Add your subplot
ax = fig.add_subplot(1,1,1)
# Change color of plot background
ax.set_facecolor((0.05,0.0,0.1))

# Create a scatter plot with black background
ax.scatter(x,y,color(0.54,0.70,0.72))
plt.show()
# Create a figure
fig = plt.figure()
# Add your subplot
ax = fig.add_subplot(1,1,1, projection='3d')
# Change color of plot background
ax.set_facecolor((0.05,0.0,01))

# Create a scatter plot with black background
ax.scatter(x,y,z,color=(1.0,1.0,1.0))
plt.show()


