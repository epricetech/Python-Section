# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 11:38:23 2023

@author: geron
"""
#lambda is a one-line shorthand for a function

add_two = lambda my_input: my_input + 2

print(add_two(3))
print(add_two(100))
print(add_two(-2))


#checks to see if a string is a substring of a string.  words that are called are checked against the is_substring 
is_substring = lambda my_string: my_string in "This is the master string"

print(is_substring('I'))
print(is_substring('am'))
print(is_substring('the'))
print(is_substring('master'))

#an if statement in lambda function creation
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A..'
print(check_if_A_grade(91))
print(check_if_A_grade(70))
print(check_if_A_grade(20))

#checks to see if there is an a in the word
#Write your lambda function here
contains_a = lambda word: 'a' in word
print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))



#Write your lambda function here
long_string = lambda word: len(word) > 12

print(long_string("short"))
print(long_string("photosynthesis"))


# can get a character by index number starting at 0
my_string = "Whoa! A seesaw"
print(my_string[0])
print(my_string[2])
print(my_string[-1])

# see if it ends in a using index
#Write your lambda function here
ends_in_a = lambda letter: letter[-1] == 'a'

print(ends_in_a("data"))
print(ends_in_a("aardvark"))


#doing math with lambda
add_or_subtract = lambda input_number: input_number - 1 if input_number >= 0 else input_number + 1

print(add_or_subtract(0))

print(add_or_subtract(8))

print(add_or_subtract(-4))



#see if it is double or zero
#Write your lambda function here
double_or_zero = lambda num: num * 2 if num > 10 else 0
print(double_or_zero(15))
print(double_or_zero(5))



#Even or odd
#Write your lambda function here
even_or_odd = lambda num: 'even' if num % 2 == 0 else 'odd' 

print(even_or_odd(10))
print(even_or_odd(5))



#checking to see if it is a multiple
#Write your lambda function here
multiple_of_three = lambda num: 'multiple of three' if num % 3 == 0 else 'not a multiple'
print(multiple_of_three(9))
print(multiple_of_three(10))



##movie rating
#Write your lambda function here
rate_movie = lambda rating: 'I liked this movie' if rating > 8.5 else 'This movie was not very good'

print(rate_movie(9.2))
print(rate_movie(7.2))


#find the integer
#Write your lambda function here
ones_place = lambda num: num % 10

print(ones_place(123))
print(ones_place(4))



#square a number by using * or ** 
#Write your lambda function here
double_square = lambda num: num ** 2 * 2


print(double_square(5))
print(double_square(3))


#random number plus variable
import random
#Write your lambda function here
add_random = lambda num: num + random.randint(1,10)
print(add_random(5))
print(add_random(100))


stringlambda = lambda x: x.lower()
print(stringlambda("Oh Hi Mark!"))


mylambda = lambda x: (x * 2) + 3
print(mylambda(5))


mylambda = lambda x: x[0]+x[-1]
print(mylambda('Hello World'))



mylambda = lambda x: 'Welcome to BattleCity!' if x >= 13 else 'You must be 13 or older'


#using the string method .split()
#df['Email Provider'] = df.Email.apply(
 #   lambda x: x.split('@')[-1])


import pandas as pd

df = pd.read_csv('employees.csv')

# Add columns here
get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name)

print(df)


# If we want to add in the price with tax for each line, we’ll need to look at two columns: Price and Is taxed?.

# If Is taxed? is Yes, then we’ll want to multiply Price by 1.075 (for 7.5% sales tax).

# If Is taxed? is No, we’ll just have Price without multiplying it.

# We can create this column using a lambda function and the keyword axis=1:

df['Price with Tax'] = df.apply(lambda row:
     row['Price'] * 1.075
     if row['Is taxed?'] == 'Yes'
     else row['Price'],
     axis=1
)

#regular function option
def total_earned(row):
   if row['hours_worked'] <= 40:
       return row['hours_worked'] * \
           row['hourly_wage']
   else:
        return (40 * row['hourly_wage'])\
            + (row['hours_worked'] - 40) * \
            (row['hourly_wage'] * 1.50)


#lamba option of function above


import pandas as pd

df = pd.read_csv('employees.csv')

total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
  if row.hours_worked > 40 \
  else row.hourly_wage * row.hours_worked

df['total_earned'] = df.apply(total_earned, axis = 1)

print(df)
   
import pandas as pd

orders = pd.read_csv('shoefly.csv')

print(orders.head(5))

orders['shoe_source'] = orders.shoe_material.apply(lambda x: \
                        	'animal' if x == 'leather'else 'vegan')

orders['salutation'] = orders.apply(lambda row: \
                                    'Dear Mr. ' + row['last_name']
                                    if row['gender'] == 'male'
                                    else 'Dear Ms. ' + row['last_name'],
                                    axis=1)

