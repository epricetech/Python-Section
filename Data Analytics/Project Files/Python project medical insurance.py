# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:43:50 2023

@author: geron
"""

# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is " + str(insurance_cost) + " dollars")


# Add insurance estimate formula below


# Age Factor
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is " + str(new_insurance_cost) + " dollars")
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("People who are 4 years older have estimated insurance costs that are " + str(change_in_insurance_cost) + " dollars different")
# BMI Factor
age = 28
bmi += 3.1
new_insurance_cost_bmi = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost_bmi = new_insurance_cost_bmi - insurance_cost
print("The change in estimate insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost_bmi) + " dollars different")

# Male vs. Female Factor
bmi = 26.2
sex = 1
new_insurance_cost_men = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("The change in estimate insurance cost for men instead of female is " + str(new_insurance_cost_men) + " dollars different")
sex_factor_rates = new_insurance_cost_men - insurance_cost
print("The difference between a man and woman with same stats is " + str(sex_factor_rates))