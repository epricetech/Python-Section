# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 09:27:58 2023

@author: geron
"""

import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1
#What do coach ticket prices look like? What are the high and low values? What would be considered average? Does $500 seem like a good price for a coach ticket?What do coach ticket prices look like? What are the high and low values? What would be considered average? Does $500 seem like a good price for a coach ticket?
sns.histplot(flight.coach_price)
plt.show()
plt.clf()
print(np.mean(flight.coach_price))
print(np.median(flight.coach_price))
print(np.min(flight.coach_price))
print(np.max(flight.coach_price))
## Task 2
#Now visualize the coach ticket prices for flights that are 8 hours long. What are the high, low, and average prices for 8-hour-long flights? Does a $500 ticket seem more reasonable than before?
#You can subset the data within the desired plotting function. For example, if we wanted to plot the histogram of coach flight prices for flights with less than 200 passengers, we would use this code:

#sns.histplot(flight.coach_prices[flight.passengers <= 200])
#plt.show() # Show the plot
#plt.clf() # Clear the plot
#You can calculate the mean or median of a subset of data using a similar method:

#np.mean(flight.coach_prices[flight.passengers <= 200])
#Once you’ve correctly plotted coach ticket prices for flights that are 8 hours long as well as some summary statistics, think about where $500 now falls in the distribution: Is it close or far from the center of the plot? Is $500 closer to the summary statistics than it was before? This would indicate a more normal or reasonable price.

sns.histplot(flight.coach_price[flight.hours == 8])
plt.show()
plt.clf()
print(np.mean(flight.coach_price[flight.hours == 8]))
print(np.median(flight.coach_price[flight.hours == 8]))
print(np.min(flight.coach_price[flight.hours == 8]))
print(np.max(flight.coach_price[flight.hours == 8]))


## Task 3
#How are flight delay times distributed? Let’s say there is a short amount of time between two connecting flights, and a flight delay would put the client at risk of missing their connecting flight. You want to better understand how often there are large delays so you can correctly set up connecting flights. What kinds of delays are typical?

#hint  If you plot a histogram of flight delay times, you’ll see that this visualization is difficult to read because of extreme outliers. Try subsetting the data to only include flight delays at a lower, more reasonable value to be able to see the distribution. Use the method mentioned in the hint of Task 2 to subset your data to specific ranges.
#It may take some trial-and-error to settle on a value as your cut-off, so you may have to try a few different values until one seems right.
#After subsetting the data by delay times, we can see that a 10-minute delay is fairly common for this airline. You will want to keep that in consideration when setting up a connecting flight.

sns.histplot(flight.delay[flight.delay <=700])
plt.show()
plt.clf()
print(np.mean(flight.delay))
print(np.median(flight.delay))
print(np.min(flight.delay))
print(np.max(flight.delay))
## Task 4
#Create a visualization that shows the relationship between coach and first-class prices. What is the relationship between these two prices? Do flights with higher coach prices always have higher first-class prices as well?
perc = 0.1
flight_sub = flight.sample(n = int(flight.shape[0]*perc))
sns.lmplot(x='coach_price', y='firstclass_price', data=flight_sub,line_kws={'color': 'black'}, lowess=True)
plt.show()
plt.clf()
## Task 5
#What is the relationship between coach prices and inflight features— inflight meal, inflight entertainment, and inflight WiFi? Which features are associated with the highest increase in price?
#You might also try using side-by-side boxplots for each inflight feature. This would show the difference in the median and spread between the flights that have an inflight feature and those that do not.
sns.histplot(flight, x='coach_price', hue=flight.inflight_meal)
plt.show()
plt.clf()
sns.histplot(flight, x='coach_price', hue=flight.inflight_entertainment)
plt.show()
plt.clf()
sns.histplot(flight, x='coach_price', hue=flight.inflight_wifi)
plt.show()
plt.clf()

## Task 6
#How does the number of passengers change in relation to the length of flights?
#You might start with a scatterplot of hours and passengers, but you would see that there are too many points in the same place, making it difficult to get information from the plot. You might want to add jitter to help spread the points out and better understand density. If the plot is still too dense to really interpret, you might consider using a subset of data instead of the full dataset.
#One thing you might notice at this point is that there are significantly fewer data points at 6 and 8 hours compared to the other hours. This is an interesting observation to notice and you might explore this fact further.
#Another thing you might notice is that there is a break in the distribution of passengers around 180 (very few flights have around 180 passengers). You might consider exploring the data points with more than 180 passengers separate from data points with less than 180 passengers and see if any trends emerge.

sns.lmplot(x = "hours", y = "passengers", data = flight_sub, x_jitter = 0.25, scatter_kws={"s": 5, "alpha":0.2}, fit_reg = False)
plt.show()
plt.clf()

## Task 7
#Visualize the relationship between coach and first-class prices on weekends compared to weekdays.
#The scatterplot showing the relationship between coach and first-class prices doesn’t show the difference between weekend flights and weekday flights. Changing the color of points by weekend status using hue will help visualize this relationship.
#As noted before, this is a really dense scatterplot, so you might consider using a subset of data to make it easier to see relationships in the data.
#We can see that on average, weekend tickets are more expensive than weekday tickets. However, based on this plot it seems like it’s easier to get a good deal on a first-class ticket on a weekday than on a weekend: the price difference between first-class and coach level tickets is larger on the weekend than on a weekday.
sns.lmplot(x = 'coach_price', y = 'firstclass_price', hue = 'weekend', data = flight_sub, fit_reg=False)
plt.show()
plt.clf()


## Task 8
#How do coach prices differ for redeyes and non-redeyes on each day of the week?
#A regular boxplot of coach prices by day of the week shows some relationship between weekday and weekend prices, but nothing about redeye flights. You can use hue to separate each day into two groups: redeyes and regular flights on that day of the week.
#We can see more clearly that the difference between redeyes and non-redeyes is pretty much the same on any day of the week, though on average weekend flights cost more than weekday flights.


