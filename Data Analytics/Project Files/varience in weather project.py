# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:11:20 2023

@author: geron
"""

import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

#print(london_data.head())
#  will print rows 100-199
#print(london_data.iloc[100:200])

print(len(london_data))

temp = london_data['TemperatureC']

#We can now calculate descriptive statistics about this column. To begin, find the average temperature in London in 2015. Store it in a variable named average_temp.temperature_var
average_temp = np.mean(temp)

#Calculate the variance of the temperature column and store the results in the variable temperature_var. Print the results.
temperature_var = np.var(temp)
print(temperature_var)

#Calculate the standard deviation of the temperature column and store a variable named temperature_standard_deviation. Print this variable.
temperature_standard_deviation = np.std(temp)
print(temperature_standard_deviation)

#We want to filter by the "month" column! The following line of code will create a variable that gets the temperature from the rows where "month" is 6. These will be all of the rows from the month of June.
june = london_data.loc[london_data['month']==6]['TemperatureC']
july = london_data.loc[london_data['month']==7]['TemperatureC']

#Calculate and print the mean temperature in London for both June and July using the np.mean() function.
print(np.mean(june))
print(np.mean(july))


#If you want to quickly see the mean and standard deviation of every month, use this block of code.
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")








