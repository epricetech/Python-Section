# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 10:25:56 2023

@author: geron
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3

berkeley = pd.read_csv("berkeley_data.csv")


colleges = list(set(berkeley.Department))
colleges.sort()
female_accept = berkeley.percent_accepted_department[berkeley.Sex == 'Female']
male_accept = berkeley.percent_accepted_department[berkeley.Sex == 'Male']
n = 1 # This is our first dataset 
t = 2 # Number of dataset
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar

x_1 = [t*element + w*n for element in range(d)]
bar1 = plt.bar(x_1, male_accept)
n = 2  
x_2 = [t*element + w*n for element in range(d)]
bar2 = plt.bar(x_2, female_accept)
plt.xlabel('Department')
plt.ylabel('Percent Accepted')
plt.legend((bar1, bar2), ('Male', 'Female'), title = "Sex", loc="upper right")
ax = plt.subplot()
ax.set_xticks((np.array(x_1) + np.array(x_2))/2)

ax.set_xticklabels(colleges)
plt.show()


#now through seaborn


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import codecademylib3

berkeley = pd.read_csv("berkeley_data.csv")

ax = sns.barplot(x = "Department", y = "percent_accepted_department", hue = "Sex", data = berkeley)
ax.set(xlabel="Department", ylabel = "Percent Accepted")
plt.show()
