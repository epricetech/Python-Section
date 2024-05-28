# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 11:31:38 2023

@author: geron
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn

import glob

#It will be easier to inspect this data once we have it in a DataFrame. You can’t even call .head() on these csvs! How are you supposed to read them?
#Using glob, loop through the census files available and load them into DataFrames. Then, concatenate all of those DataFrames together into one DataFrame, called something like us_census
files = glob.glob('states*.csv')
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)
us_census = pd.concat(df_list)

#step 3
print(us_census.head())
print(us_census.dtypes)

#step 4
#Use regex to turn the Income column into a format that is ready for conversion into a numerical type.
# i kinda understand the loop and the replace_dol but i dont
# really understnd .iat[index] part or why remove a , i didnt
# really see it in the data
for index in range(0,len(us_census["Income"])):
    string = str(us_census['Income'].iat[index])
    replace_dol = string.replace('$', '')
    replace_com = replace_dol.replace(',', '')
    us_census['Income'].iat[index] = replace_com

us_census["Income"] = pd.to_numeric(us_census['Income'])
us_census["Income"]
print(us_census.head())
print(us_census.dtypes)

# Step 6
#Look at the GenderPop column. We are going to want to separate this into two columns, the Men column, and the Women column.
#Split the column into those two new columns using str.split and separating out those results.
# I went a different direction got it split but couldnt figure out the rest
Men = []
Women = []
for index in range(0,len(us_census["GenderPop"])):
    string = str(us_census['GenderPop'].iat[index])
    replace = string.split('_')
    Men.append(replace[0])
    Women.append(replace[1])

us_census['Men'] = Men
us_census['Women'] = Women
print(us_census.head())

#Step 7

#Convert both of the columns into numerical datatypes.
#There is still an M or an F character in each entry! We should remove those before we convert.

for index in range(0,len(us_census["Men"])):
    string = str(us_census['Men'].iat[index])
    replace = string.replace('M', '')
    us_census['Men'].iat[index] = replace
    
for index in range(0,len(us_census["Women"])):
    string = str(us_census['Women'].iat[index])
    replace = string.replace('F', '')
    us_census['Women'].iat[index] = replace
    
us_census['Men'] = pd.to_numeric(us_census['Men'])
us_census['Women'] = pd.to_numeric(us_census['Women'])

print(us_census.head())

#Step 8 
plt.scatter(us_census['Women'], us_census['Income'])
plt.title("Scatter Plot of Income vs. Number of Women per State")
plt.xlabel("Population of Women per State")
plt.ylabel("Income (in US Dollars)")
plt.show()
plt.clf()

#Step 9
#You want to double check your work. You know from experience that these monstrous csv files probably have nan values in them! Print out your column with the number of women per state to see.
#We can fill in those nans by using pandas’ .fillna() function.
#You have the TotalPop per state, and you have the Men per state. As an estimate for the nan values in the Women column, you could use the TotalPop of that state minus the Men for that state.
#Print out the Women column after filling the nan values to see if it worked!

print(us_census['Women'])
us_census['Women'] = us_census['Women'].fillna(us_census['TotalPop'] - us_census['Men'])
print(us_census['Women'])

#step 10
#We forgot to check for duplicates! Use .duplicated() on your census DataFrame to see if we have duplicate rows in there.
us_census.duplicated(subset = us_census.columns[1:])


#Step 11
#Drop those duplicates using the .drop_duplicates() function.
census = us_census.drop_duplicates(subset = us_census.columns[1:])
census

#Step 12
plt.scatter(us_census['Women'], us_census['Income'])
plt.title("Scatter Plot of Income vs. Number of Women per State")
plt.xlabel("Population of Women per State")
plt.ylabel("Income (in US Dollars)")
plt.show()
plt.clf()

#Step 14  - create a histogram for each ethnic
#Try to make a histogram for each one!
#You will have to get the columns into numerical format, and those percentage signs will have to go.
#Don’t forget to fill the nan values with something that makes sense! You probably dropped the duplicate rows when making your last graph, but it couldn’t hurt to check for duplicates again.
# this part cleans the data and removes % and missing data
for race in ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']:
    for index in range(0,len(us_census)):    
        string = str(us_census[race].iat[index])
        replace = string.replace('%', '')
        if (replace == "nan"):
            replace = ""
        us_census[race].iat[index] = replace
    us_census[race] = pd.to_numeric(us_census[race])
    
us_census['Pacific'] = us_census['Pacific'].fillna(100 - us_census['Hispanic'] - us_census['White'] - us_census['Black'] - us_census['Native'] - us_census['Asian'])

census = us_census.drop_duplicates(subset = us_census.columns[1:])
census
#  this loop creates the same histo for each column
for race in ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']:
    plt.hist(census[race])
    plt.title("Histogram of the Percentage of {} People per State".format(race))
    plt.xlabel("Percentage")
    plt.ylabel("Frequency")
    plt.show()
    plt.clf()




