# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:34:35 2023

@author: geron
"""

import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head(10))
print(cart.head(10))
print(checkout.head(10))
print(purchase.head(10))

visits_cart = visits.merge(cart, how='left')
print(visits_cart)
len_visit_cart = len(visits_cart)
print(len_visit_cart)

null_time = len(visits_cart[visits_cart.cart_time.isnull()])
print(null_time)

visit_not_cart = float(null_time) / float(len_visit_cart)
print(visit_not_cart)

cart_checkout = cart.merge(checkout, how='left')
print(cart_checkout)
null_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])
print(null_checkout)

cart_not_checkout = float(null_checkout) / float(len(cart))
print('Cart but not checkout ', cart_not_checkout)

all_data = visits_cart.merge(cart_checkout, how='left').merge(purchase, how='left')
print(all_data.head(10))

reach_checkout = all_data[~all_data.purchase_time.isnull()]
checkout_nosale = all_data[(all_data.purchase_time.isnull()) & (~all_data.checkout_time.isnull())]
checkout_nosale_percent = float(len(checkout_nosale)) / float(len(reach_checkout))
print('% of users who got to checkout but didnt buy ', checkout_nosale_percent)

print("{} percent of users who visited the page did not add a t-shirt to their cart".format(round(visit_not_cart*100, 2)))
print("{} percent of users who added a t-shirt to their cart did not checkout".format(round(cart_not_checkout*100, 2)))
print("{} percent of users who made it to checkout  did not purchase a shirt".format(round( checkout_nosale_percent*100, 2)))



all_data['time_to_buy'] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_buy)

print(all_data.time_to_buy.mean())