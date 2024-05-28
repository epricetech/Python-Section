# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:17:40 2023

@author: geron
"""

from matplotlib import pyplot as plt
import csv

def convert_time_to_num(time):
  mins = int(time[-2:])
  frac_of_hour = mins/60.0
  hour = int(time[:-3])
  time = hour + frac_of_hour
  return time

sales_times_raw = []
with open('sales_times.csv') as csvDataFile:
  csvReader = csv.reader(csvDataFile)
  for row in csvReader:
    sales_times_raw.append(row[2])
  sales_times_raw = sales_times_raw[1:]

sales_times = []
for time in sales_times_raw:
  sales_times.append(convert_time_to_num(time))
  
  
  
  
  
  
  import numpy as np
import matplotlib as mpl
load_file_in_context('histogram.py')

bar_heights = [rect.get_height() for rect in plt.gca().get_children() if isinstance(rect, mpl.patches.Rectangle)]

if len(bar_heights) == 11:
  expected_heights = [25.0, 19.0, 30.0, 23.0, 30.0, 29.0, 19.0, 26.0, 37.0, 32.0, 1.0]
  if not np.array_equal(bar_heights, expected_heights):
    fail_tests("Make sure to plot the `sales_times` array as the input to `plt.hist`.")
else:
  fail_tests('Your histogram should have 10 bins, but your seems to have {} bins.'.format(len(bar_heights)))

pass_tests()



from matplotlib import pyplot as plt
import csv

def convert_time_to_num(time):
  mins = int(time[-2:])
  frac_of_hour = mins/60.0
  hour = int(time[:-3])
  time = hour + frac_of_hour
  return time

sales_times_raw = []
with open('sales_times.csv') as csvDataFile:
  csvReader = csv.reader(csvDataFile)
  for row in csvReader:
    sales_times_raw.append(row[2])
  sales_times_raw = sales_times_raw[1:]

sales_times1 = []
for time in sales_times_raw:
  sales_times1.append(convert_time_to_num(time))

sales_times2_raw = []
with open('sales_times_s2.csv') as csvDataFile:
  csvReader = csv.reader(csvDataFile)
  for row in csvReader:
    sales_times2_raw.append(row[2])
  sales_times2_raw = sales_times2_raw[1:]

sales_times2 = []
for time in sales_times2_raw:
  sales_times2.append(convert_time_to_num(time))






#  this is from the multiple imputation section of cleaning data

import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import pandas as pd

d = {
    'D': [6.9,np.nan,5.4,4.7,4.5,5.1,4.1,4.5,np.nan,7.5],
    'E': [18.5,21.9,np.nan,21.2,12.4,16.7,11,11.5,21.6,np.nan],
    'F': [np.nan,36.3,50.6,48.7,51.9,np.nan,51.6,50.1,46.9,36.6],
    'G': [80,70.1,94.5,np.nan,76.3,84.6,np.nan,93.6,68.9,82]
}

dTest = {
    'D': [5.6,np.nan,4.5,3.2,5.9],
    'E': [16.1,20.7,np.nan,22.4,13.4],
    'F': [np.nan,31.2,53.2,47.8,50.8],
    'G': [79.9,71.3,92.4,np.nan,75.6]
}

# Define df and dfTest as pandas DataFrames 
df = pd.DataFrame(data=d)
dfTest = pd.DataFrame(data=dTest)

# Create the IterativeImputer model to predict missing values
imp = IterativeImputer(max_iter=10, random_state=0)

# Fit the model to the first few rows
imp.fit(dfTest)

# Transform the model on the entire dataset
dfComplete = pd.DataFrame(np.round(imp.transform(df),1), columns=['D','E','F','G'])

# Uncomment the following statement to print the result
print(round(dfComplete.mean(),2))

