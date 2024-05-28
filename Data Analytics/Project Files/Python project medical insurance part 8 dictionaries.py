# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:09:04 2023

@author: geron
"""

# Add your code here
#Empty dicitonary
medical_costs = {}
#add key and value indivually
medical_costs['Marina'] = 6607.0
medical_costs['Vinay'] = 3225.0
#add multiple key and values at the same time
medical_costs.update({'Connie':8886.0, 'Isaac':16444.0, 'Valentina':6420.0})
print(medical_costs)

medical_costs.update({'Vinay':3325.00})
print(medical_costs)
#goes through list and adds all the costs together for find average.  .values() will get all the values for the keys in the dictionary.  So the for loop is getting the value for each key in the dictionary
total_cost = 0
for cost in medical_costs.values():
  total_cost += cost
average_cost = total_cost / len(medical_costs)
print('Average Insurance Cost: ' + str(average_cost))  

names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [37, 24, 43, 35, 52]
#combines 2 lists together
zipped_ages = zip(names, ages)
#takes that combined list and sets a key and value for dictionary
names_to_ages = {key:value for key, value in zipped_ages}
print(names_to_ages)
#get specific info from dictionary
marina_age = names_to_ages.get('Marina', None)
print("Marina's age is " + str(marina_age))

medical_records = {}
#adds an entry for a single key with multiple dictionaries of data
medical_records['Marina'] = {'Age': 27, 'Sex': 'Female', 'BMI': 31.1, 'Children': 2, 'Smoker': 'Non-Smoker', 'Insurance_cost': 6607.0}

medical_records['Vinay'] = {'Age': 24, 'Sex': 'Male', 'BMI': 26.9, 'Children': 0, 'Smoker': 'Non-Smoker', 'Insurance_cost': 3225.0}

medical_records['Connie'] = {'Age': 43, 'Sex': 'Female', 'BMI': 25.3, 'Children': 3, 'Smoker': 'Non-Smoker', 'Insurance_cost': 8886.0}

medical_records['Issac'] = {'Age': 35, 'Sex': 'Male', 'BMI': 20.6, 'Children': 4, 'Smoker': 'Smoker', 'Insurance_cost': 16444.0}

medical_records['Valentina'] = {'Age': 52, 'Sex': 'Female', 'BMI': 18.7, 'Children': 1, 'Smoker': 'Non-Smoker', 'Insurance_cost': 6420.0}

print(medical_records)
#to print out specific info for connie
print("Connie's insurance cost is " + str(medical_records['Connie']['Insurance_cost']) + " dollars.")
#to get info for issac
issac_info = medical_records["Issac"]['BMI']
print('This is Issac BMI ' + str(issac_info))

medical_records.pop('Vinay')
# To loop the dictionary and print all the info.  use the .items to get both key and value from dictionary
for name, record in medical_records.items():
  print(name + " is a " + str(record["Age"]) + \
  " year old " + record["Sex"] + " " + record["Smoker"] \
  + " with a BMI of " + str(record["BMI"]) + \
  " and insurance cost of " + str(record["Insurance_cost"]))


















