# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 13:09:10 2023

@author: geron
"""

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

knicks_pts_10 = nba_2010[nba_2010.fran_id == 'Knicks']['pts']
nets_pts_10 = nba_2010[nba_2010.fran_id == 'Nets']['pts']
#print(knicks_pts_10)
#print(nets_pts_10)

diff_mean_2010 = knicks_pts_10.mean() - nets_pts_10.mean()
print(diff_mean_2010)


plt.hist(knicks_pts_10, alpha=0.8, normed = True, label='knicks')
plt.hist(nets_pts_10, alpha=0.8, normed = True, label='nets')
plt.legend()
plt.title("2010 Season")
plt.show()


knicks_pts_14 = nba_2014[nba_2014.fran_id == 'Knicks']['pts']
nets_pts_14 = nba_2014[nba_2014.fran_id == 'Nets']['pts']
#print(knicks_pts_10)
#print(nets_pts_10)

diff_mean_2014 = knicks_pts_14.mean() - nets_pts_14.mean()
print(diff_mean_2014)


plt.hist(knicks_pts_14, alpha=0.8, normed = True, label='Knicks')
plt.hist(nets_pts_14, alpha=0.8, normed = True, label='Nets')
plt.legend()
plt.title("2014 Season")
plt.show()

sns.boxplot(data=nba_2010, x='fran_id', y='pts')
plt.show()

location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)

location_result_proportions = location_result_freq/len(nba_2010)
print(location_result_proportions)

chi2, pval, dof, expected=chi2_contingency(location_result_freq)
print(expected)
print(chi2)


point_diff_forcast_cov = np.cov(nba_2010.point_diff, nba_2010.forecast)
print(point_diff_forcast_cov)


point_diff_forecast_corr, p=pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)

plt.scatter(x='forecast', y='point_diff', data=nba_2010)
plt.xlabel('Forecast')
plt.ylabel('Point Difference')
plt.show()




