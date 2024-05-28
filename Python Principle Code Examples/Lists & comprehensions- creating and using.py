# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 12:31:26 2023

@author: geron
"""

# lists - are ordered collection of items between [] seperated by a comma.  
# all values in list must be same category and data type
# each value in list has an index number starting with 0.  you can call value by index by variable[index#]
# you can use - to for index number to start from the end of the list.  like variable[-1] will pull the last value in list
# you can also re-assign a value to list base on index - variable[index#] = 'new_value'
# you can also remove a value from a list - variable.remove('value')
# Another variation of lists is a  2d list which is basically a list that contains another list good for girds
# Syntax for 2d list - all values must be same category and data type
# variable = [[valuex, valuey],[value2x, value2y], [value3x, value3y]]
# example - heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]

# List Methods - methods that work on  lists
# .count() - to count the number of occurrences of an element in a list:can also be used in a 2d list with [] inside the ()
# .insert() - to insert an element into a specific index of a list - needs 2 inputs first being a numerical index 
# and the next is the data
# .pop() - to remove an element from a specific index or from the end of the list
# range() - built in function to create a sequence of integers and can be used in loops
# len() - built in function to get length of list
# .sort() / sorted() - a method and built in function to sort a list.  Can be also used in reverse.  
# Example names.sort(reverse=True)
# sorted() - it comes before a list due to being a built in function and it creates a new list rather 
# than modifying the original one.  Example - sorted_names = sorted(names)  names is the list
# list() - when you use range you must convert with built in function especially when you output the 
# data with print or return

# creating a list from multiple variables using zip() and list() methods
# example 
# names = ["Jenny", "Alexus", "Sam", "Grace"]
# heights = [61, 70, 67, 64]
# names_and_heights = zip(names, heights)
# converted_list = list(names_and_heights)
# print(converted_list)

# Splicing - when you want to extract a portion of a list
# syntax
# variable = list_variable{[:6]} - which says start at index 0 and go to index 6 and stop if you did {[3:]} it would 
# start at index 3 and go through to the end of the list
# the first digit is where to start and the last is the indext number to stop.  


# examples of lists - empty lists a list that can be set up to a 2d list and one that should be split due to data type
ints_and_strings = [1, 2, 3, "four", "five", "six"]
sam_height_and_testscore = ["Sam", 67, 85.5, True]
my_empty_list = []

# a way to combine to lists together
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]
# Create new orders here:
new_orders = ["lilac", "iris"]
orders_combined = orders + new_orders

# create a 2d list and also how to change values in list  using index
incoming_class = [["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]
print(incoming_class)

incoming_class[2][2] = 8
print(incoming_class)

incoming_class[-3][-3] = "Ken"
print(incoming_class)

# example of using the .append method to add to a list
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)

# example 2 d list with removal of values in list, adding to the list and changing a value in the list
customer_data = [["Ainsley", "Small", True], ["Ben",  "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

customer_data[2][-1] = False

customer_data[1].remove(False)

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]

print(customer_data_final)


# examples of splicing lists
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:2]
print(beginning)

middle = suitcase[2:4]
print(middle)

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)


# List Method Examples

# example .insert method
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)
 
front_display_list.insert(0, 'Pineapple')
print(front_display_list)

# example .pop method - which removes items from list
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(3)
print(data_science_topics)

# examples of range method and list method to convert
# using the range function - if you add a 3rd element in range that is how much it will incriment
number_list = range(9)
print(list(number_list))
zero_to_seven = range(8)
print(list(zero_to_seven))

my_range2 = range(2, 9, 2)
print(list(my_range2))

# example of len method
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
big_range = range(2, 3000, 100)

long_list_len = len(long_list)
print(long_list_len)

big_range_length = len(big_range)
print(big_range_length)

# example of count method
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

jake_votes = votes.count("Jake")
print(jake_votes)

# examples of sort method
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)
# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
print(names)

# example of sorted method - puts in in order
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

games_sorted = sorted(games)
print(games)
print(games_sorted)

# Example remove method
shopping_line = ["Cole", "Kip", "Chris","Sylvana", "Chris"]
shopping_line.remove("Chris")
print(shopping_line)

# example of multiple lists and 2d lists with using append to combine
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]
gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]
print(gradebook)
gradebook.append(('computer science', 100))
gradebook.append(('visual arts', 93))
gradebook[1][1] = 99
gradebook[2].remove(85)
gradebook[2].append('Pass')
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)

# example - overall use of list with methods and setting values by index and combining lists
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
num_pizzas = len(toppings)
print('We sell ', num_pizzas, ' different kinds of pizza!')

pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]
pizza_and_prices.sort()
print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop(-1)
pizza_and_prices.insert(4, [2.5, 'peppers'])
print(pizza_and_prices)
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]
names_and_heights = zip(names, heights)
print(names_and_heights)

converted_list = list(names_and_heights)
print(converted_list)


# example of function that sorts a list
def combine_sort(my_list1, my_list2):
  unsorted = my_list1 + my_list2
  sortedList = sorted(unsorted)
  return sortedList

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# example of function with list appends
def append_sum(my_list):
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  return my_list

print(append_sum([1, 1, 2]))

# example function that removes a portion of a list
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# example function with count method
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# example function that uses append and index number
def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    new_lst = lst[0:index]
  new_lst.append(lst[index]*2)

  new_lst = new_lst + lst[index+1:]
  return new_lst

print(double_index([3, 8, -10, 12], 2))


# example function that go through list and does some math to results
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))

# example list for tarot reading
tarot = { 1:"The Magician", 2:"The High Priestess", 3:"The Empress", 4:"The Emperor", 5:"The Hierophant", 
         6:"The Lovers", 7:"The Chariot", 8:"Strength", 9:"The Hermit", 10:"Wheel of Fortune", 11:"Justice",
         12:"The Hanged Man", 13:"Death", 14:"Temperance", 15:"The Devil", 16:"The Tower", 17:"The Star", 
         18:"The Moon", 19:"The Sun", 20:"Judgement", 21:"The World", 22:"The Fool"}
spread = {}

spread['past'] = tarot.pop(13)
spread['present'] = tarot.pop(22)
spread['future'] = tarot.pop(10)

for key, value in spread.items():
  print('Your ' + key + ' is the ' + value + ' card.')

# example list with append sort calling by index len and str methods
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records = list(zip(names, insurance_costs))
print(medical_records)

num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records")

first_medical_record = medical_records[0]
print("Here is the first medical record: " + str(first_medical_record))

medical_records.sort()
print("Here are the medical records sorted by insurance cost: " + str(medical_records))

cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records:" + str(cheapest_three))

priciest_three = medical_records[-3:]
print("Here are the most expensive insurance costs in our medical records:" + str(priciest_three))

# function with for in range and if statements - finding the same values
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))



# - going through lists with function and for range and if statements reversed list matching
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

# combine 2 lists into a dictionary
# syntax students = {key:value for key, value in zip(names, heights)} - using zip takes lits into tuples with elements paired together

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key:value for key, value in zip(names, heights)}
print(students)


drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)


# list comprehensions - another way to write lists and loops
# syntax
#variable = [<expression>] for <element> in <collection>]
# expression is a variable you create in statement
# element is the same as the expression
# colleciton is the variable you want to run through with for statement

numbers = [2, -1, 79, 33, -45]
doubled = []
 
for number in numbers:
  doubled.append(number * 2)
 
print(doubled)

# same code as above but in list comprehension format.  
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)


grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)


# a more normal way to write this code
numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []
 
for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)
 
print(only_negative_doubled)


# this option is using list comprehensions

numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)


# another way using an if and else statement
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)


#how the syntax changes between using for, if and else statements
numbers = [2, -1, 79, 33, -45]
 
no_if   = [num * 2 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 2 if num < 0 else num * 3 for num in numbers]



heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)












