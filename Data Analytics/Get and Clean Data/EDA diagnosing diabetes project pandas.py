# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:43:26 2023

@author: geron
"""

import codecademylib3
import pandas as pd
import numpy as np

# code goes here

diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data)

print(diabetes_data.isnull().sum())
print(diabetes_data.describe())
#replaces 0 for nan
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)
print(diabetes_data.describe())

print(diabetes_data.isnull().sum())
#prints all the null values
print(diabetes_data[diabetes_data.isnull().any(axis=1)])
print(diabetes_data.dtypes)

print(diabetes_data.Outcome.unique())

diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O', '0')
print(diabetes_data.Outcome.unique())