# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:54:03 2023

@author: geron
"""

import pandas as pd

inventory = pd.read_csv('inventory.csv')
#print(inventory.head(10))

staten_island = inventory.head(10)
#print(staten_island)

product_request = staten_island.product_description
#print(product_request)

seed_request = inventory[(inventory.product_type == 'seeds') & (inventory.location == 'Brooklyn')]
print(seed_request)

inventory['in_stock'] = inventory.apply(lambda row: True
    if row.quantity > 0 else False, axis=1)


inventory['total_value'] = inventory.apply(lambda row: row.quantity * row.price)




combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
    

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory.head(10))