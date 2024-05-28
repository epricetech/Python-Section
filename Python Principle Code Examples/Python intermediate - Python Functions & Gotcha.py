# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 10:21:29 2023

@author: geron
"""

# There are times when working with functons you are tempted to include an emput list as a default argument
#  example would be a function that creates a dictionary of students name, age and grades

def createStudent(name, age, grades=[]):
    return {
        'name': name,
        'age': age,
        'grades': grades}
# lets add 2 students without the grade aspect
chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

# now lets add grades for the 2
def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])
addGrade(chrisley, 90)
addGrade(dallas, 100)

# now the issue here is the output - the first student is correct however the grades for the 2nd student shows both values
# and not the specific value that was assigned.  This is called GOTCHA
# the key principle is to remember these are nutable objects which means that they are intended to change
# a list and dictionaries are 2 mutable objects in python
# when using mutable in function arguments the Default parameter values are evaluated from left to right when the 
# function definition is executed. # This means that the expression is evaluated once, when the function
#  is defined, and that the same
 # “pre-computed” value is used for each call.
# the immutable objects are int, floats and tuples

# This means that when we call a function, the default values we provide for parameters are only created once, 
# and used for each subsequent call of the function. This means our grades=[] from our earlier function was 
# only created once and anytime we tried to access it, the same list was being modified. We can even see that 
# the memory id of the grades property for both students is the same (using the built-in id() function):

# The ids printed will vary depending on the computer we are using. 
print(id(chrisley['grades']))
print(id(dallas['grades']))
# output provides the same id number for both


# The NONE Workaround for the GOTCHA issue
# when you want and empty list to be a defualt argument in a funciton you must assigne None value to argument
# you need an if statement to check the none value
def createStudent(name, age, grades=None):
  if grades is None:
    grades = []
  return {
    'name': name,
    'age': age,
    'grades': grades}
 
def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])
chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)
addGrade(chrisley, 90)
addGrade(dallas, 100)
# output assigns the grade value and only that value to the correct student

# example of using an empty dictionary and adding values through function and no Gotcha values
tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables)
def assign_table(table_number, name, vip_status=False): 
  tables[table_number] =  [name, vip_status]
assign_table(6, 'Yoni', False)
print(tables)
assign_table(table_number=3, name='Martha', vip_status=True)
print(tables)
assign_table(4, 'Karla')
print(tables)


# Variable number of arguments - * args or any name but must have * to define and not use when calling
# there is an additional operator called the unpacking operator *
# this allows us to give our functions a variable number of arguments by performing a positional argument packing
# example that uses basic unpacking operator
def my_function(*args):
  print(args)
# if we called the function with random arguments
my_function('Arg1', 245, False)
# output would be the values we called
# example
def print_order(*order_items):
  print(order_items)
print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')


#  how to use positional arument packing
# this will unpack the positional variables and also do an upper method on the values in the function call
def shout_strings(*args):
  for argument in args:
    print(argument.upper())
shout_strings('Working on', 'learning', 'argument unpacking!')

# you can also add arguments in addition to the unpacking operator
def truncate_sentences(length, *sentences):
  for sentence in sentences:
    print(sentence[:length])
truncate_sentences(8, "What's going on here", "Looks like we've been cut off")
# this is the break down of the code above for understanding
# We have two parameters that our function truncate_sentences() defines. The first is a length parameter that will 
# specify how many characters we want to keep. The second is a parameter called sentences that is paired with the 
# unpacking operator, signifying it will take a variable number of arguments.
# On each iteration of the function, we are looping through the tuple created by the sentences argument
#  (because it is paired with the unpacking operator) and performing a slice on the sentence based on the 
#  provided length argument. This forces every value in the sentences tuple to be cut down in length.

# example of unpacking - functions and setting values for dictionary
tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)
def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''

def assign_and_print_order(table_number, *order_items):
  tables[table_number]['order'] = order_items
  for orders in order_items:
    print(orders)
assign_table(2,'Arwa', True)
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')
print(tables)



# Variable number of keyword arguments using **kwargs - but allows us to forcus on key and not value in dictionary

def arbitrary_keyword_args(**kwargs):
  print(type(kwargs))
  print(kwargs)
  # See if there's an 'anything_goes' keyword arg and print it
  print(kwargs.get('anything_goes'))
arbitrary_keyword_args(this_arg='wowzers', anything_goes=101)
# since **kwargs is a dictionary we can use standard dictionary functions like .get() to retrieve values

# example of ** argument and adding to the dictionary
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)
def assign_food_items(**order_items):
  print(order_items)
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  print(food)
  print(drinks)
# Example Call
assign_food_items(food='Pancakes, Poached Egg', drinks='Water')

# working with **kwargs - very similar to *args we can use the .values() method to iterate through the ** diciontary

def print_data(**data):
  for arg in data.values():
    print(arg)
print_data(a='arg1', b=True, c=100)

# all positional arguments must come first before the **
def print_data(positional_arg, **data):
  print(positional_arg)
  for arg in data.values():
    print(arg)
print_data('position 1', a='arg1', b=True, c=100)

# example of function with positional and keyword arguments
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}
assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks
print('\n --- tables after update --- \n')

assign_food_items(2, food = 'Seabass, Gnocchi, Pizza', drinks = 'Margarita, Water')
print(tables)


# combing both * and ** for arguments
# argument order in a function are
# 1. Standard positional argument
# 2. * args
# 3. standard keyword argument
# 4. **kwargs
#example
def print_animals(animal1, animal2, *args, animal4, **kwargs):
  print(animal1, animal2)
  print(args)
  print(animal4)
  print(kwargs)
print_animals('Snake', 'Fish', 'Guinea Pig', 'Owl', animal4='Cat', animal5='Dog')
# # breakdown of above code
# The first two arguments that our function accepts will take the form of standard positional arguments. 
# When we call the function, the first two values provided will map to animal1 and animal2. Thus, the first
#  line of output is Snake Fish
# The non-keyword arguments that follow after Snake and Fish in our function call are all mapped to the args tuple. 
# Thus, our result is ('Guinea Pig', 'Owl')
# Then we transition to regular keyword arguments. Since we called animal4 as a keyword, our result for the print 
# statement is Cat
# Lastly, we have one more keyword argument that is mapped to **kwargs. Thus, our last line of
#  output is {'animal_5': 'Dog'}

# Write your code below: 
def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
  print(appetizer)
  print(entrees)
  print(sides)
  print(dessert_scoops)

single_prix_fixe_order('Baby Beets', 'Salmon', 'Scallops', sides='Mashed Potatoes', ice_cream_scoop1 = 'Vanilla', ice_cream_scoop2 = 'Cookies and Cream')


#  Not only can we use * and ** operators in our function defination we can use them in our function calls as well
# when using the unpacking operator * we are spreading the list into individual argumens in our function definition
#  this can save the ahssle of writing loops and is more flexable
my_num_list = [3, 6, 9]
def sum(num1, num2, num3):
  print(num1 + num2 + num3)
sum(*my_num_list)
# Or
numbers  = {'num1': 3, 'num2': 6, 'num3': 9}
def sum(num1, num2, num3):
  print(num1 + num2 + num3)
sum(**numbers)


# we can also use the operators inside of built in functions like range()
start_and_stop = [3, 6]
range_values = range(*start_and_stop)
print(list(range_values))

#Unpacking parts of an iterable
a, *b, c = [3, 6, 9, 12, 15]
print(b)
#Would output: [6, 9, 12]
#Merging iterables
my_tuple = (3, 6, 9)
merged_tuple = (0, *my_tuple, 12)
print(merged_tuple)
#Would output: (0, 3, 6, 9, 12)
#Combining unpacking and packing
num_collection = [3, 6, 9]
def power_two(*nums): 
  for num in nums:
    print(num**2)
power_two(*num_collection)
#Would output:9 36 81

# example
def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  print(split_price)
table_7_total = [534.50,20.0,5]
calculate_price_per_person(*table_7_total)







