# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 07:27:35 2023

@author: geron
"""

import codecademylib3

# 1
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
# Create restaurants dataframe
restaurants = pd.read_csv('restaurants.csv')
# Inspect restaurant dataframe
print(restaurants.head())
# Check number of unique cuisines
print(restaurants['cuisine'].nunique())
# Group count by cuisine
cuisine_count = restaurants.groupby('cuisine').name.count().reset_index()

# Inspect cuisine_counts dataframe
print(cuisine_count)
# Create a pie chart
plt.pie(cuisine_count.name.values,labels=cuisine_count.values,autopct='%d%%')
plt.axis('equal')
plt.title('Cuisines')
plt.show()
# 2
# Create orders dataframe
orders = pd.read_csv('orders.csv')

# Inspect the orders dataframe
print(orders.head())

# Create new month column
orders['month'] = orders.date.apply(lambda x: x.split('-')[0])
# Inspect new orders dataframe
print(orders.head())

# Create average order by month dataframe
avg_order = orders.groupby('month').price.mean().reset_index()
# Inspect avg_order dataframe
print(avg_order)
# Create standard deviation dataframe
std_order = orders.groupby('month').price.std().reset_index()
# Inspect std_order
print(std_order)
# Create barplot
ax = plt.subplot()
plt.bar(range(len(avg_order)),avg_order.price,yerr=std_order.price,capsize = 5)
ax.set_xticks(range(len(avg_order)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.ylabel('Average order amount')
plt.title('Average Order Amount over Time')
plt.show()
# 3
# Create customer amount dataframe
customer_amount = orders.groupby('customer_id').price.sum().reset_index()
# Inspect customer amount
print(customer_amount)
# Create histogram
plt.hist(customer_amount.price.values,range=(90,200),bins=40)
plt.xlabel('Total Spent')
plt.ylabel('Number of Customers')
plt.title('Money Money Money')
plt.show()



