# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:30:00 2023

@author: geron
"""

import pandas as pd

orders = pd.read_csv('shoefly.csv')

print(orders.head())

emails = orders.email

frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

print(frances_palmer)

comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]