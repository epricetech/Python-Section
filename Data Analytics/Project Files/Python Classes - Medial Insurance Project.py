# -*- coding: utf-8 -*-
"""
Created on Mon May  8 08:58:03 2023

@author: geron
"""


#  bulding the class constructor

class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
    # add more parameters here
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker)

##Now that our constructor is built out and ready to go, let’s start creating some methods! Our first method will be estimated_insurance_cost(), which takes our instance’s parameters (representing our patient’s information) and returns their expected yearly medical fees.
##Below the __init__ constructor, define our estimated_insurance_cost() constructor which only takes self as an argument. Inside of this method, add the following formula:  estimated_cost=250∗age−128∗sex+370∗bmi+425∗num_of_children+24000∗smoker−12500

def estimated_insurance_cost(self):
  estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
  print(self.name + "'s estimated insurance costs is "+ str(estimated_cost) + ' dollars.')
print(estimated_insurance_cost(patient1))

def update_age(self, new_age):
  self.age = new_age
  print(self.name + ' is now ' + self.new_age + ' years old.')
  patient1.update_age(26)
  self.estimated_insurance_cost()

def update_num_children(self,new_num_children):
  self.num_of_children = new_num_children
  print(self.name + ' has ' + self.new_num_children + ' children.')
  patient1.update_num_children(1)
  if self.num_of_children == 1:
  print(self.name + " has " + str(self.num_of_children) + "child.")
else:
  print(self.name + " has " + str(self.num_of_children) + "children.")

Reminder that to call estimated_insurance_cost() in your update_num_children() method use the following line of code:

self.estimated_insurance_cost()
To call the update_num_children() with patient1 use the following line of code:

# note: you can try any number when calling the method
patient1.update_num_children(1)
In your output terminal you should see the following:

John Doe has 1 child
John Doe's estimated insurance cost is 2511.0  

# initialize empty dictionary
patient_information = {}
# set name as a key tied with the name value
patient_information[“name”] = self.name
Your patient_profile() method should look similar to the following example:

def patient_profile(self):
  patient_information = {}
  patient_information["Name"] = self.name
  patient_information["Age"] = self.age
  patient_information["Sex"] = self.sex
  patient_information["BMI"] = self.bmi
  patient_information["Number of Children"] = self.num_of_children
  patient_information["Smoker"] = self.smoker
  return patient_information

print(patient1.patient_profile())
In the output terminal you should see the following information:

{'Name': 'John Doe', 'Age': 26, 'Sex': 1, 'BMI': 22.2, 'Number of Children': 1, 'Smoker': 0}


