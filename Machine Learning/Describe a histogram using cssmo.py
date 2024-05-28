# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:51:59 2023

@author: geron
"""

#  5 features of a dataset for the histogram.  Called cssmo  - center, spread, skew, modality, outliers

# center - use the average and median for measurement of centality  
#example

import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import codecademylib3_seaborn

cp_data = pd.read_csv("cp.csv") 

cp_average = cp_data[' Average Covered Charges '].mean()

cp_median = cp_data[' Average Covered Charges '].median()

plt.hist(cp_data[' Average Covered Charges '], bins=20, edgecolor='black')

plt.title("Distribution of Chest Pain Treatment Cost by Hospital", fontsize = 16)
plt.xlabel("Cost ($)", fontsize = 16)
plt.ylabel("Count", fontsize = 16)
plt.axvline(cp_average, color='r', linestyle='solid', linewidth=2, label="Mean")
plt.axvline(cp_median, color='y', linestyle='solid', linewidth=2, label="Median")
plt.legend()

plt.show()


#  spread  - the min and max values of the dataset  find range by taking max-min

# Skew - is the shape of the data.  Skew is the description of the datas symmetry  - normal distribution = symmetric


# modality - desribes the number of peaks in a dataset.  unimodel, bimodal, multimodel 

# outliers - data point that is far away from the rest of the dataset.  dont have a formal definition


