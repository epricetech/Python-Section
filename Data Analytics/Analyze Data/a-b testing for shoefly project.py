# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:22:42 2023

@author: geron
"""

import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head(10))

most_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(most_views)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isull()
#The ~ is a NOT operator, and isnull() tests whether or not the value of ad_click_timestamp is null.

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().reset_index()

clicks_pivot = clicks_by_source.pivot(
  columns='is_click',
  index='utm_source',
  values='user_id'
).reset_index()

print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
# clicks_pivot[True] is the number of people who clicked (because is_click was True for those users)

# clicks_pivot[False] is the number of people who did not click (because is_click was False for those users)

# So, the percent of people who clicked would be (Total Who Clicked) / (Total Who Clicked + Total Who Did Not Click)

num_people = ad_clicks.groupby('experimental_group').user_id.count().reset_index
print(num_people)

percent = ad_clicks.groupby(['is_click', 'experimental_group']).user_id.count().reset_index().pivot(
    columns='is_click',
    values='user_id',
    index='experimental_group').reset_index()
print(percent)

a_click = ad_clicks[ad_clicks.experimental_group == 'A']
b_click = ad_clicks[ad_clicks.experimental_group == 'B'
                    
                    
a_clicks_pivot = ad_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
    columns='is_click',
    index='day',
    values='user_id').reset_index()

a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])
print(a_clicks_pivot)
print(b_clicks_pivot)


                   
                    
                    
                    ]
