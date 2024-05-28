# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 11:09:27 2023

@author: geron
"""

import pandas as pd
import numpy as np
car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head(5))

counts = car_eval['manufacturer_country'].value_counts()
print(counts)

proportions = car_eval['manufacturer_country'].value_counts(normalize=True)
print(proportions)

print(car_eval['buying_cost'].unique())

buy_cost_categories = ['low', 'med','high','vhigh']
print(buy_cost_categories)

car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'],buy_cost_categories,ordered=True)
print(car_eval.buying_cost)

median = np.median(car_eval['buying_cost'].cat.codes)
print(median)
median_category = buy_cost_categories[int(median)]
print(median_category)

luggage_proportion = car_eval['luggage'].value_counts( normalize=True)
print(luggage_proportion)

include_nan = car_eval['luggage'].value_counts(dropna=False, normalize=True)
print(include_nan)

replicate = car_eval['luggage'].value_counts()/len(car_eval.luggage)
print(replicate)

replicate2 = car_eval['luggage'].value_counts()/car_eval['luggage'].count()


frequency = (car_eval.doors == '5more').sum()
print(frequency)

proportion = (car_eval.doors == '5more').mean()
print(proportion)
