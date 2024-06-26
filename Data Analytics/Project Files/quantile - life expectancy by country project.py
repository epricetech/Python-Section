# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 08:57:26 2023

@author: geron
"""

import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")

print(data.head())

life_expectancy = data['Life Expectancy']

life_expectancy_quartiles = np.quantile(life_expectancy,[.25,.5,.75])
print(life_expectancy_quartiles)

#plt.hist(life_expectancy)
#plt.show()

gdp = data['GDP']
median_gdp = np.quantile(gdp,.5)

low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] > median_gdp]

low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'],[.25,.5,.75])
print(low_gdp_quartiles)
high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'],[.25,.5,.75])
print(high_gdp_quartiles)

plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()


