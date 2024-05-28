# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:49:23 2023

@author: geron
"""

# plotting bar charts using seaborn    import seaborn as sns    use the sns.countplot(df['x parameter']) or barplot()


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("games.csv")
print(df.head())

sns.countplot(df['victory_status'])

#  for nominal data
#  this line will order the bar chart in ascending order - to do decending just get rid of the ascending=True
sns.countplot(df["victory_status"], order=df["victory_status"].value_counts(ascending=True).index)

#  for ordinal data
# part of the sns.countplot() function with order paramater
sns.countplot(df["Grade Level"], order=["First Year", "Second Year", "Third Year", "Fourth Year"])





import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("school_data.csv")
print(df.head())

value_order = ["NOT ENOUGH DATA", "VERY WEAK", "WEAK", "NEUTRAL", "STRONG", "VERY STRONG"]

type_of_data = "ordinal"


# plot using .countplot() method here
sns.countplot(df['Supportive Environment'], order=value_order)
plt.xticks(rotation=30)

# show your plot here
plt.show()



#  pie charts for categorical data - used to show proportions
#  Steps to take     1.  create 2 variables that point the the colums of data you want.  2.  plot pie with labels paramater
#  Then clean up chart with title legend ect ect 

import matplotlib.pyplot as plt
import pandas as pd
import codecademylib3

water_usage = pd.read_csv("water_usage.csv")
print(water_usage.head())

wedge_sizes = water_usage['prop']
pie_labels = water_usage['water_source']

plt.pie(wedge_sizes, labels=pie_labels)
plt.axis('equal')
plt.title('Distribution of House Water Usage')

plt.show()


#  same as above but in a bar chart using the barplot() function
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import codecademylib3

pie_data = pd.read_csv("pie_data.csv")

graph_counts = pie_data["values"]

graph_labels = pie_data["labels"]

plt.subplot(1,2,1)
plt.pie(graph_counts, labels = graph_labels)
plt.axis('Equal')
plt.title("Tough to Compare")

plt.subplot(1,2,2)
sns.barplot(graph_labels,graph_counts)
plt.title("Easy to Compare")

plt.show()







import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import codecademylib3

major_data = pd.read_csv("major_data.csv")
print(major_data.head())

major_data_agg = pd.read_csv("major_data_agg.csv")
print(major_data_agg.head())

pie_wedges = major_data["proportion"]
pie_labels = major_data["major"]

pie_wedges_agg = major_data_agg["proportion"]
pie_labels_agg = major_data_agg["department"]

plt.subplot(2,1,1)
plt.pie(pie_wedges, labels = pie_labels)
plt.axis('Equal')
plt.title("Too Many Slices")
plt.tight_layout()

plt.subplot(2,1,2)
plt.pie(pie_wedges_agg, labels=pie_labels_agg)
plt.axis('Equal')
plt.title("Good Number of Slices")
plt.tight_layout()

plt.show()

















