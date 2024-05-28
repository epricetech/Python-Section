# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 07:52:51 2023

@author: geron
"""

import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")

print(healthcare.head())

#print(healthcare['DRG Definition'].unique())
#Seperates out the value of 313 chest pain from the column
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']

#  to get every chest pain code in state of al
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == 'AL']

oregon_chest_oain = chest_pain[chest_pain['Provider State'] == 'OR']

#  Get costs of chest pain in AL
costs = alabama_chest_pain[' Average Covered Charges '].values
#plt.boxplot(costs)
#plt.show()

# to find costs for all states to comopare to each other
states = chest_pain['Provider State'].unique()

# loop through all the states
datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain['Provider State']==state][' Average Covered Charges '].values)

# to set size of boxplot
plt.figure(figsize=(20,6))

plt.boxplot(datasets, labels = states)
plt.show()


