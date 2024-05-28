# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:08:29 2023

@author: geron
"""


#using scatter vizualize for 2 quantiative variables
# plt.scatter(x = housing.price, y = housing.sqfeet)
# plt.xlabel('Rental Price (USD)')
# plt.ylabel('Area (Square Feet)')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt 

housing = pd.read_csv('housing_sample.csv')

print(housing.head())

#create your scatter plot here:
plt.scatter(x=housing.beds, y=housing.sqfeet)
plt.xlabel('Number of beds')
plt.ylabel('Square Feet')


plt.show()






