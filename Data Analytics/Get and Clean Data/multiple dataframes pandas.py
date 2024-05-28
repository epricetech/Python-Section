# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 08:09:33 2023

@author: geron
"""

#pd.merge() to merge 2 dataframes and look for common values
#syntax
#variable = pd.merge(df1, df2)
# each datafram has its own .merge()
#variable = df.merge(df2)
# Example of multiple dataframes merge
# Variable = df1.merge(df2).merge(df3)

import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

sales_vs_targets = pd.merge(sales,targets)
print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]



import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

men_women = pd.read_csv('men_women_sales.csv')

all_data = sales.merge(targets).merge(men_women)

print(all_data)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)] 



#To rename column when you need to merge and you need them unique
pd.merge(
    orders,
    customers.rename(columns={'id': 'customer_id'}))


import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(orders, products.rename(columns={'id': 'product_id'}))


print(orders_products)


#when the column names dont always match and sometime new columns are created.  suffixes renaes them to be more accurate
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(orders, products,
  left_on = 'product_id',
  right_on = 'id',
  suffixes = ['_orders', '_products'])

#outer merge when you have mismatching rows and lose data during normal merge.  will show all rows
#pd.merge(company_a, company_b, how='outer')

import pandas as pd

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)


store_a_b_outer = pd.merge(store_a,store_b,how='outer')
print(store_a_b_outer)

#left and right merge 
import pandas as pd

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

store_a_b_left = pd.merge(store_a, store_b, how='left')
print(store_a_b_left)

store_b_a_left = pd.merge(store_b,store_a,how='left')
print(store_b_a_left)


#combining smaller dataframes into a single big one.  like if each location had a csv file for email.  use concat to put it all in one file

import pandas as pd

bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)

menu = pd.concat([bakery,ice_cream])
print(menu)



