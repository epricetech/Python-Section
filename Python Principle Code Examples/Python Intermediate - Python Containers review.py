# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:19:06 2023

@author: geron
"""

#  Containers are ways to store and orgamize data.  Any type of object that stores data is a container.  
#  Built in containers are lists, dictionaries, tuples and sets.  These containers each specialize in a specific job and 
# can be imported into your code from other moduels or even custom made.  
#  common built in containers

# Lists -  an ordered group of elements that can be added, removed, accessed, and modified
products = ['t-shirt', 'pants', 'shoes', 'dress', 'blouse']
 
products.append('jacket')
products.sort()
products.remove('shoes')

# Tuples - are immutable objects which group multiple elements together.  Similiar to lists but cant bemodified
searched_terms = ('clothes', 'phone', 'app', 'purchase', 'clothes', 'store', 'app', 'clothes')
 
term = searched_terms[2]
num_of_occurrences = searched_terms.count('clothes')

# Dictionaries - unordered  groups ofkey-value pairs
orders = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99}, 
          'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99}
         }
 
order_4829_price = orders['order_4829']['price']
order_6184_size = orders['order_6184']['size']
orders['order_4829']['size'] = 'x-large'
num_of_orders = len(orders)

# Sets - unordered group of elements that cant contain duplicates and cant be modified
old_products_set = {'t-shirt', 'pants', 'shoes'}
new_products_set = {'t-shirt', 'pants', 'blouse', 'dress'}
updated_products = new_products_set | old_products_set
removed_products = old_products_set - new_products_set



# Specialized Containers
# The previous containers were all built in containers.  Specialized containers come from the collenctions module
#  which you must import.  Each of these specialized containers focuses on a certain improvement to its built in 
# counterparts.  Example of import collections module
# To import a single class or multiple classes
from collections import name_of_class, name_of_another_class
 
# To import all classes in the collections module
from collections import *
 
# Another way to import all classes in a module
import collections


# example of OrderedDict specialized container
from collections import OrderedDict
 
orders = OrderedDict({'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99},
          'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99},
          'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}})
 
orders.move_to_end('order_4829')
orders.popitem()


# # Advanced Containers
# deque
# namedtuple
# Counter
# defaultdict
# OrderedDict
# ChainMap


# Deque - similar to lists but they are optimized for appending and popping to the front and back rather than just accessing
# these deque containers are used for working with data where you dont need to access alements in the middle very often
#  can be used instead of lists when you need to prioritize and move elements in a specific order.  Example a bug report
# for software where you want the high priority moved to the top of the list and then removed when complete
# example of doing this with a list vs a deque container
# list example
bug_data = []
loaded_bug_reports = get_all_bug_reports()
for bug in loaded_bug_reports:
    if bug['priority'] == 'high':
        # A list uses the insert method to append to the front
        bug_data.insert(0, bug)
    else:
        bug_data.append(bug)
# A list must provide an index to pop
next_bug_to_fix = bug_data.pop(0)

# compared to deque example
from collections import deque
bug_data = deque()
loaded_bug_reports = get_all_bug_reports()
for bug in loaded_bug_reports:
    if bug['priority'] == 'high':
        # With a deque, we can append to the front directly
        bug_data.appendleft(bug)
    else:
        bug_data.append(bug)
# With a deque, we can pop from the front directly
next_bug_to_fix = bug_data.popleft()


# example and instructions for deque container
from helper_functions import process_csv_supplies
from collections import deque

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]
# Write your code below!

supplies_deque = deque()
#Using a for loop, read each item from csv_data. On each iteration, if the item is marked as important, append it to the front of supplies_deque, otherwise append it to the end.
for row in csv_data:
  if row[2] == 'important':
    supplies_deque.appendleft(tuple(row))
  else:
    supplies_deque.append(tuple(row))
#Your accountant let you know that you have enough of a budget to order 25 important materials and 10 unimportant materials.
#For this step, create a new deque called ordered_important_supplies. Remove the first 25 important items from your supplies_deque and append them to ordered_important_supplies.
ordered_important_supplies = deque()
for material in range(25):
  ordered_important_supplies.append(supplies_deque.popleft()) 
#Now that you have completed the orders for the 25 important items, repeat the same process for 10 unimportant items.
#Create a new deque called ordered_unimportant_supplies. Remove 10 low important items from your supplies_deque and append them to ordered_unimportant_supplies
ordered_unimportant_supplies = deque()
for unimport in range(10):
  ordered_unimportant_supplies.append(supplies_deque.pop())


# Named Tuple - Specialized container
# Useful for grouping together data that does not need to be modified in the future.  However Tuples have issues
#  when they host various data and even nested data.  
# example of a tuple
actor_data_tuple = ('Leonardo DiCaprio', 1974, 'Titanic', 1997)
#While the tuple does a great job of creating a container that can keep ordered immutable data, it can become quite 
# confusing to represent properties using numerical indices. For example:
actor_data_tuple[3]
# Unless we explicitly define a variable name that describes what the third index represents, it’s very 
# hard to tell what data we are talking about. We would also need to make separate variables for each property!

# nametuple allows us to have an immutable tuple object but every element becomes self-documented
#  example of nametuple which will work better than a normal tuple example above
from collections import namedtuple
# General Structure: namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
ActorData = namedtuple('ActorData', ['name', 'birth_year', 'movie', 'movie_release_date'])
# In this example, we are defining an instance of the namedtuple collection with a typename called 'ActorData' and a
#  sequence of strings called field_names that represent the labels for the data we want to store.

# We are saying we want our namedtuple to be called 'ActorData' and for it to have name, birth_year, movie, and 
# movie_release_date properties. It’s like creating a label system for the type of data inside of the tuple!

# We can then define an instance of our ActorData:

actor_data = ActorData('Leonardo DiCaprio', 1974, 'Titanic', 1997)
# This then allows us to access the mapped property value to its associated name from before using the . notation:

# print(actor_data.name)
# Would return:

# Leonardo DiCaprio

# key aspects of namedtupe container
# You may have noticed we use a CapWords convention when defining our namedtuple. 
# This is because namedtuple actually returns a subclass and thus falls under the conventions we use for classes.
# The field_names argument can alternatively be a single string with each fieldname separated by 
# whitespace and/or commas, for example, 'x y' or 'x, y'.
# At first glance, namedtuples might seem like it is trying to replicate a dictionary. 
# While the key idea of labeling properties is the same in both structures, namedtuples have some key 
# advantages over a regular dictionary:
# They are immutable and maintain their order, while a dictionary does not.
# They are more lightweight than dictionaries and take no more memory than a regular tuple.


# overall example of namedtuple and instructions of what is going on
clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

# Write your code below!
#Import the container and create a namedtuple subclass called ClothingItem with a typename of 
# 'ClothingItem' and the field_name consisting of: 'type', 'color', 'size', and 'price' in that specific order.
from collections import namedtuple
ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size', 'price'])

#Let’s test out our new ClothingItem namedtuple subclass!
#For this checkpoint, create a new object from the subclass ClothingItem called new_coat.
#The new_coat should have a type of 'coat', a color of 'black', a size of 'small', and a price of 14.99.
new_coat = ClothingItem('coat', 'black', 'small', 14.99)
#Now that the new_coat object has been created, access the price of this namedtuple object and store it in a 
# variable called coat_cost.
coat_cost = new_coat[3]
# #There is too much manual work when creating the namedtuple objects one at a time, so lets use a loop!
# #We have a list of tuples containing clothing information called clothes.
# #First, create a new empty list called updated_clothes_data and then for every piece of clothes data in the
#  list of tuples, append a new ClothingItem object to updated_clothes_data while passing the data from the tuple 
#  into the new ClothingItem object.
updated_clothes_data = []
for elem in clothes:
   updated_clothes_data.append(ClothingItem(elem[0], elem[1], elem[2], elem[3]))
print(updated_clothes_data)



# DefaultDict container
#  When dealing with dictionaries one of the most common issues is how to deal with missing keys.  When a key doesnt
# exist it will throw a KeyError.  
#  Example of a dictionary with a kay value missing
prices = {'jeans': 19.99, 'shoes': 24.99, 't-shirt': 9.99, 'blouse': 19.99}
print(prices['jacket'])
# output
# KeyError
#  defaultDict will help solve this issued by having a default missing value in the dictionary.  
#  example of this concept
#  first step is to inport the class and set the default value - can use lambda function or just defualtdict('defaultstring')
from collections import defaultdict
validate_prices = defaultdict(lambda: 'No Price Assigned')
# Then we can set the keys and values like a regular dictionary
validate_prices['jeans'] = 19.99
validate_prices['shoes'] = 24.99
validate_prices['t-shirt'] = 9.99
validate_prices['blouse'] = 19.99
#  now we can access an invalid key to observe the results
print(validate_prices['jacket'])
# output - will run the lambda function which is the defualt key, because the key jacket doesnt exist in the dictionry
# No Price Assigned

# overall example and instructions of what is happening
site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

# Write your code below!
#We are updating an old version of our website to include new products that we have for sale. 
# We have a dictionary of all of the previous products and locations on our site. The team has 
# provided a list of all products our company sells including the new additions which are randomly 
# placed within the list. Use a defaultdict to validate which products are on the site and to automatically 
# label those which are missing. For products which are missing, their values should default to 'TODO: Add to website'.
# #For this first checkpoint, import the defaultdict class from the collections module and create a new 
# variable called validated_locations. Use the defaultdict constructor to create a new defaultdict
#  object in validated_locations which defaults missing keys to have a value of 'TODO: Add to website'.
from collections import defaultdict
validated_locations = defaultdict(lambda: 'TODO: Add to website')
#Not only can we create a defaultdict from scratch, but we can also create one from an existing dictionary. 
# To do this, we can use the .update() method from the defaultdict class. This behaves the same way 
# as the .update() method from the dict class.
#Take a look at the Python documentation for a refresher on the .update() method.
#site_locations represents where each product exists on the clothing store website.
#Use the .update() method to move all of the site_location data into validated_locations.
validated_locations.update(site_locations)
#We need to update the original dictionary with the new information. Iterate through every item in
 # the updated_products list and update the site_locations dictionary with the values from validated_locations.
for item in updated_products:
  site_locations[item] = validated_locations[item]
print(site_locations)



# OrderedDict Container
# When dealing with many different dictionaries issues might arise.  In some cases you can store a dictionary in a list
#  when this is done the order is preserved but to acceess the elements by their index before we can access the dictionary
#  example of this concept
first_order = {'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}}
second_order = {'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99}}
third_order = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99}}
list_of_dicts = [first_order, second_order, third_order]
# In order to get the price for a specific order we must know the index of it already before we can acces the dictionary
# data stored inside which can be time consuming and ineeficient
print(list_of_dicts[1]['order_6184']['price'])
# Output
# 14.99
#  also another issue is being able to move elements around.  Even though a dictionary is ordered
dict_of_dicts = {}
dict_of_dicts.update(first_order)
dict_of_dicts.update(second_order)
dict_of_dicts.update(third_order)
print(dict_of_dicts['order_6184']['price'])
# Output
# 14.99

# OrderedDict allows us to access values using keys, but it also preserves the order of the elements
#  example of using OrderedDict
from collections import OrderedDict
orders = OrderedDict()
## the order of the data is preserved when additing to the OrderedDict
orders.update({'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}})
orders.update({'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99}})
orders.update({'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99}})
# data can be accessed using keys like a normal dictionary instead of indexes when you put a dicitonary into a list liek above examples
# Get a specific order
find_order = orders['order_2905']
# the order can be retireved by converting it to a list then accessing by index
# Get the data in a list format
orders_list = list(orders.items())
third_order = orders_list[2]
# OrderedDict has methods for moving the data around.  We can move an element to the back or front and pop the data
# from the back or front
# Move an item to the end of the OrderedDict
orders.move_to_end('order_4829')
 
# Pop the last item in the dictionary
last_order = orders.popitem()
# these 2 methods also accept boolean arguments which deterrmine if the element is moved or popped 

# example of OrderedDict and instuctions
from collections import OrderedDict

# The first 15 orders are provided
order_data = [['Order: 1', 'purchased'],
              ['Order: 2', 'purchased'],
              ['Order: 3', 'purchased'],
              ['Order: 4', 'returned'],
              ['Order: 5', 'purchased'],
              ['Order: 6', 'canceled'],
              ['Order: 7', 'returned'],
              ['Order: 8', 'purchased'],
              ['Order: 9', 'returned'],
              ['Order: 10', 'canceled'],
              ['Order: 11', 'purchased'],
              ['Order: 12', 'returned'],
              ['Order: 13', 'purchased'],
              ['Order: 14', 'canceled'],
              ['Order: 15', 'purchased']]

# Write your code below!
#We want to add some logic to our application which will organize orders by their status. A list of orders is 
# provided which includes the order number and the status. The status of an order can be purchased, returned,
#  or canceled. To make things more organized, we want to remove the canceled orders and push the returned 
#  orders to the end. In order to do this, we can use an OrderedDict!
# #For this first checkpoint, import the OrderedDict class and create a new object from that class called orders.
#  Use the constructor to automatically convert the order_data into an OrderedDict.
# from collections import OrderedDict
orders = OrderedDict(order_data)
#We need to keep track of which orders to remove and which ones to push back. To do this, 
# create two new lists called to_move and to_remove. Iterate through each item in orders and check what 
# the status is. If the status is 'returned' then add the key (order number string) to the to_move list. 
# Otherwise, if the status is 'canceled' then add it to the to_remove list.
to_move = []
to_remove = []
for key, val in orders.items():
  if val == 'returned':
    to_move.append(key)
  elif val == 'canceled':
    to_remove.append(key)

#Now that we have the list of items to remove from orders, for every item in the to_remove list, .pop() the
 # element from orders.
for item in to_remove:
  orders.pop(item)

#Now that all of the canceled orders have been removed, use another loop to push back any of the 'returned'
 # orders from to_move to the end of orders. This will be similar to the last step, but this time we are
 # using the .move_to_end() method.
for item in to_move:
  orders.move_to_end(item)
print(orders)



# ChainMap
#  another way to store dictionaries or other mappings byond using defualtDict and OrderedDict
#  ChainMap container allows us to store many mappings in an ordered group, but accessing the value using a key
# are repeated for every mapping inside of the ChainMap until something is found of the end is reached
#  In ChainMap if we modify the data in any way then only the fist mapping will recieve the changes
#  When accessing data Chainmap terats all the stored dictionaries as one large dictionary where if there are
# repeated keys, then the first found result is returned only.
# example of ChainMap
from collections import ChainMap
customer_info = {'name': 'Dmitri Buyer', 'age': '31', 'address': '123 Python Lane', 'phone_number': '5552930183'}
shirt_dimensions = {'shoulder': 20, 'chest': 42, 'torso_length': 29}
pants_dimensions = {'waist': 36, 'leg_length': 42.5, 'hip': 21.5, 'thigh': 25, 'bottom': 18}
# next we inialize the ChainMap with the mappings which we want to use.  Example mappings are dimensions dicitonarys
customer_data = ChainMap(customer_info, shirt_dimensions, pants_dimensions)
# now we can access values from any of the stored mappings
customer_leg_length = customer_data['leg_length']
# The parents property skips the first mapping and returns everything else(all of the parents of the fist mapping)
customer_size_data = customer_data.parents
# we can directly modify the data only in the first dictionary
customer_data['address'] = '456 ChainMap Drive'
# in order to modify data from dictionaries which are deeper in the ChainMap we will need to iterate through
# the dictionaries which are stored inside of it
# in above example we create a new ChainMap using 3 different dictionaries.  This allows us to access any of the key:value pairs stored inside
#  ChainMap uses the concept of parent mapping.  If we used the .parents property, all mappings except the 
#  first one will be returned.  This is becuase those mappings are considered to be the parent mappings to the first one
#  we can add a new child mapping to the front of the list of mappings using the .new_child() method


# example of Chainmap with insturctions of what is going on
year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

# Write your code below!
#Our business has been doing well over the past year and we have been provided with a list of dictionaries representing the amount of profit per month as well as additional profit from holidays when applicable. We want an easy way to monitor our profit over the most recent 12 month period. To do this, we can use the ChainMap class. This will allow us to conserve historical data while also allowing us to retrieve the most recent data. It will even allow us to work with additional keys within dictionary updates.
#First, remember to import ChainMap. Then create a new ChainMap called profit_map using the year_profit_data list. Remember that a ChainMap accepts a variable number of arguments so we need to expand the list (*) so the constructor will read them as individual arguments instead of one single argument.
from collections import ChainMap
profit_map = ChainMap(*year_profit_data)

#For the next step, we need logic which will be able to calculate the normal profits and the holiday profits separately. Create a function called get_profits which calculates the sum of the standard profits (keys not containing 'holiday') and the holiday profits (keys containing 'holiday') in two different variables. Make this function return the two variables: the standard profit first and the holiday profit second. Additionally, call the function using the profit_map and store the results in variables called last_year_standard_profit and last_year_holiday_profit.
def get_profits(input_map):
    total_standard_profit = 0.0
    total_holiday_profit = 0.0

    for key in input_map.keys():
        if 'holiday' in key:
            total_holiday_profit += input_map[key]
        else:
            total_standard_profit += input_map[key]

    return total_standard_profit, total_holiday_profit
last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)

#It has been three months and our accountant has sent three more months worth of profit data in the form of a list of dictionaries called new_months_data. Add the new mappings to the profit_map so that the old January - March months are still in the ChainMap, but accessing those keys will return data for the most recent three months. Call the get_profits function on the profit_map again and store the results in current_year_standard_profit and current_year_holiday_profit to calculate the sum of the most recent 12 months of profit data.
for item in new_months_data:
    profit_map = profit_map.new_child(item)

current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)

#Finally, we want to take a look at the difference in the last 12 month period compared to the current 12 month period. Calculate the difference for the standard and holiday profits and store them in variables called year_diff_standard_profit and year_diff_holiday_profit. Print out the results to see the difference in profit for the current 12 month period.
year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit
print(year_diff_standard_profit)
print(year_diff_holiday_profit)



# Counter 
#  One of the common tasts we might need is to count instances of an element in a collection
#  Example of counting elements in a list
#  first define a list of items
clothes_list = ['skirt', 'hoodie', 'dress', 'blouse', 'jeans', 'shoes', 'skirt', 'skirt', 'jeans', 'hoodie', 'boots', 'jeans', 'jacket', 't-shirt', 'skirt', 'skirt', 'dress', 'shoes', 'blouse', 'hoodie', 'skirt', 'boots', 'shoes', 'boots', 'jeans', 'hoodie', 'blouse', 'hoodie', 'shoes', 'shoes', 'blouse', 'boots', 'blouse', 'hoodie', 't-shirt', 'jeans', 'dress', 'skirt', 'jacket', 'boots', 'skirt', 'dress', 'jeans', 'jeans', 'jacket', 'jeans', 'shoes', 'dress', 'hoodie', 'blouse']
# if we wanted to create a representation of how many of each item exisits in our collection we could use a loop
#  and a dictionary
counted_items = {}
for item in clothes_list:
   if item not in counted_items:
       counted_items[item] = 1
   else:
       counted_items[item] += 1
 
print(counted_items)
# output in not particular order
# {'skirt': 8, 'hoodie': 7, 'dress': 5, 'blouse': 6, 'jeans': 8, 'shoes': 6, 'boots': 5, 'jacket': 3, 't-shirt': 2}
#  this option above will work but Counter will allow you to accomplish same goal qucker

#  Counter - instantly counts elements for any hashable object.  It stores the data as a dictionary where the keys
# are the elements and the values are the number of occurences.  Same example as above but with Counter
from collections import Counter
counted_items = Counter(clothes_list)
print(counted_items)
# output
# Counter({'skirt': 8, 'jeans': 8, 'hoodie': 7, 'blouse': 6, 'shoes': 6, 'dress': 5, 'boots': 5, 'jacket': 3, 't-shirt': 2})

#  Addtionally the counter has methods that will help with mathematical operations for subtracting one count
# dictionary from another, finding the most common elements and generate a new list of elements based on 
# the number of occurances


# example of Counter and instructions of what is going on
opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse', 'skirt', 'skirt', 'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 'dress', 'jeans', 'dress', 'blouse']

closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 'dress', 'dress', 'jeans', 'dress', 'blouse']

# Write your code below!
#We have decided to add some more logic to our clothing store application to automatically calculate how much of each product has been sold based on our inventory at the start of the day vs the end of the day.
#First, let’s define a function called find_amount_sold. Our function will need three parameters: opening, closing, and item. For now, inside of the function, simply add the keyword return. Also, don’t forget to import the Counter class as we will be using it throughout the checkpoints.
#At this point, we could create two loops to meticulously count every item in each list, but instead, let’s create two Counter objects to calculate a count of items in our opening and closing inventory.
#Inside of our new function, and before it returns, create a variable called opening_count and store a Counter object passing in the opening parameter as the counter’s input.
#Then, create a variable called closing_count which stores a Counter object and passes in the closing parameter into the Counter.
#Next, we’ll have to subtract the closing counted data from the opening counted data in order to get the amount sold for every item. Luckily, the Counter container has a method that allows us to accomplish this really easily.
#Take a look at the Python documentation for the .subtract() method.
#When you are ready, call the .subtract() method on opening_count and pass in closing_count as the first argument.
#Awesome! Now we have our Counter object with the difference in item inventory. You may have noticed earlier we defined a parameter named item in our function declaration. This is because the goal of our function is to return the difference in inventory for a specific item rather than all of them!
#Using the parameter item, access the item’s inventory from the opening_count Counter object and return it.

from collections import Counter
def find_amount_sold(opening,closing,item):
  opening_count = Counter(opening)
  closing_count = Counter(closing)
  opening_count.subtract(closing_count)
  return opening_count[item]
#Finally, let’s test out your function by calling it with opening_inventory as the first argument, closing_inventory as the second argument, and t-shirt as the third argument.
tshirts_sold = find_amount_sold(opening_inventory,closing_inventory,'t-shirt')
print(tshirts_sold)



# Container Wrappers - 3 different wrapper containers
# UserDict
# UserList
# UserString

#  Wrappers are modifications to functions or classes which change the behavior in some way.  Most common use is on functions
#  example of a class wrapper
class Customer:
 
  def __init__(self, name, age, address, phone_number):
    self.name = name
    self.age = age
    self.address = address
    self.phone_number = phone_number
# next we create a wrapper class which stores an object of the class we are wrapping around it
class CustomerWrap(Customer):
 
  def __init__(self, name, age, address, phone_number):
    self.customer = Customer(name, age, address, phone_number)
 
  def display_customer_info(self):
    print('Name: ' + self.customer.name)
    print('Age: ' + str(self.customer.age))
    print('Address: ' + self.customer.address)
    print('Phone Number: ' + self.customer.phone_number)
#  Lastly we can create an object from the wrapper class to access the new funtionality and the wrapped class contained inside
customer = CustomerWrap('Dmitri Buyer', 38, '123 Python Avenue', '5557098603')
customer.display_customer_info()
 
# Output
# Name: Dmitri Buyer
# Age: 38
# Address: 123 Python Avenue
# Phone Number: 5557098603

#Wrapper classes allow us to create different variations of classes with different purposes while avoiding 
# duplicate code. Since we use an instance of the wrapped class inside of it, it preserves all of the attributes 
# and methods from the wrapped class and keeps us from having to re-type all of the code.


# UserDict container wrapper
#  lets us create our own version of a dictionary.  This contains all the functionality of a dictionary except
#  we can access the dictionary data through the data property.  
# example of creating a modified dictionary
from collections import UserDict
 
# Create a class which inherits from the UserDict class
class DisplayDict(UserDict):
    # A new method to increase the dictionary's functionality
    def display_info(self):
        print("Number of Keys: " + str(len(self.keys())))
        print("Keys: " + str(list(self.keys())))
        print("Number of Values: " + str(len(self.values())))
        print("Values: " + str(list(self.values())))
 
    # We can also overwrite a method from the dictionary class
    def clear(self):
        print("Deleting all items from the dictionary!")
        super().clear()
 
disp_dict = DisplayDict({'user': 'Mark', 'device': 'desktop', 'num_visits': 37})
 
disp_dict.display_info()
 
disp_dict.clear()
#As shown in this code example, we can add additional methods and overwrite methods from the UserDictclass. 
#This is the same as inheriting from regular classes in Python.

# example of UserDict and instructions of what is going on
data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

# Write your code below!
#Let’s try creating a new dictionary which is able to clear orders which are already processed when the method .clean_orders() is called. Import the UserDict class and create a new class which inherits from it called OrderProcessingDict. The .clean_orders() method should search for any keys called ‘order_status’ and if value is equal to 'complete', remove the entire order from the dictionary.
from collections import UserDict
class OrderProcessingDict(UserDict):
    def clean_orders(self):
      to_del = []
      for key, val in self.data.items():
        if val['order_status'] == 'complete':
          to_del.append(key)
      for item in to_del:
        del self.data[item]

#Now that you have created your own class, try creating an instance of it called process_dict while passing data into the constructor. Afterwards, call the .clean_orders() method to automatically clean the orders inside. You can also print your custom dictionary to see the results.
process_dict = OrderProcessingDict(data)
process_dict.clean_orders()
print(process_dict)



# UserList
#  this wrapper container allows us to create our own list.  Same functionality but has a property called data
# which allows us to access the list contents directly.  
#  Example of using the list container wrapper
from collections import UserList
 
# Create a class which inherits from the UserList class
class CondenseList(UserList):
 
    # A new method to remove duplicate items from the list
    def condense(self):
        self.data = list(set(self.data))
        print(self.data)
 
 
    # We can also overwrite a method from the list class
    def clear(self):
        print("Deleting all items from the list!")
        super().clear()
 
condense_list = CondenseList(['t-shirt', 'jeans', 'jeans', 't-shirt', 'shoes'])
 
condense_list.condense()
 
condense_list.clear()
#As shown in this code example, we can add additional methods and overwrite methods from the UserList class. 
#This is the same as inheriting from regular classes in Python.


# example of Userlist and isntructions of what is going on
data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

# Write your code below!
#Now, let’s try creating a custom list class using UserList. Create a new class called ListSorter which inherits from the UserList class. Inside of this class, overwrite the .append() method to sort the list after appending the value to it.
from collections import UserList
class ListSorter(UserList):
    def append(self, item):
      self.data.append(item)
      self.data.sort()

#Now that we have created our own list class, try creating an object using it’s constructor. Create an object called sorted_list and pass data into the ListSorter constructor. Afterwards, append the value 2 to the new object and print out the results.
sorted_list = ListSorter(data)
sorted_list.append(2)
print(sorted_list)



# UserString wrapper container
# This container wrapper is for the string class.  Contains all functionality but has property called data.
#  inheriting from this class allows us to create our own version of a string
#  example of UserString
from collections import UserString
 
# Create a class which inherits from the UserString class
class IntenseString(UserString):
 
    # A new method to capitalize and add exclamation points to our string
    def exclaim(self):
        self.data = self.data.upper() + '!!!'
        return self.data
 
 
    # Overwrite the count method to only count a certain letter
    def count(self, sub=None, start=0, end=0):
        num = 0
        for let in self.data:
            if let == 'P':
                num+=1
        return num
 
 
intense_string = IntenseString("python rules")
 
print(intense_string.exclaim())
print(intense_string.count())


# Example of UserString and instructions of what is going on
str_name = 'python powered patterned products'
str_word = 'patterned '

# Write your code below!
#Let’s create a new string class using UserString. Import the UserString class and create a new class called SubtractString which inherits from it. In this class, overwrite the - operator to remove the string on the right side of the operator from the string stored in the object. Another way to think about this is to replace the substring on the right side of the operator with an empty string.
from collections import UserString
class SubtractString(UserString):
    def __sub__(self,other):
      if other in self.data:
        self.data = self.data.replace(other, '')
  
#Now that we have created our new string class, create a new object from that class called subtract_string while passing str_name in as the argument to the constructor. Next, use the - operator to subtract the substring str_word from subtract_string.
subtract_string = SubtractString(str_name)
subtract_string - str_word
print(subtract_string)



# overall REview of Specialized containers
# deque
# An advanced container which is optimized for appending and popping items from the front and back. 
# For accessing many elements positioned elsewhere, it is better to use a list.

# namedtuple
# The namedtuple lets us create an immutable data structure similar to a tuple, but we don’t have to access the 
# stored data using indices. Instead, we can create instances of our namedtuple with named attributes. 
# We can then use the . operator to retrieve data by the attribute names.

# Counter
# This advanced container automatically counts the data within a hashable object which we pass into it’s constructor. 
# It stores it as a dictionary where the keys are the elements and the values are the number of occurrences.

# defaultdict
# An advanced container which behaves like a regular dictionary, except that it does not throw an error when
#  trying to access a key which does not exist. Instead, it creates a new key:value pair where the value defaults 
#  to what we provide in the constructor for the defaultdict.

# OrderedDict
# The OrderedDict combines the functionality of a list and a dict by preserving the order of elements, but also 
# allowing us to access values using keys without having to provide an index for the position of stored dictionaries.

# ChainMap
# This interesting container combines multiple mappings into a single container. When accessing a value using a
#  key, it will search through every mapping contained within until a match is found or the end is reached. 
#  It also provides some useful methods for grouping parent and child mappings.

# UserDict
# This is a container wrapper which lets us create our own version of a dictionary

# UserList
# This is a container wrapper which lets us create our own version of a list

# UserString
# This is a container wrapper which lets us create our own version of a string



# Overall example with instructions of what is going on
overstock_items = [['shirt_103985', 15.99],
                    ['pants_906841', 19.99],
                    ['pants_765321', 15.99],
                    ['shoes_948059', 29.99],
                    ['shoes_356864', 9.99],
                    ['shirt_865327', 10.99],
                    ['shorts_086853', 9.99],
                    ['pants_267953', 21.99],
                    ['dress_976264', 32.99],
                    ['shoes_135786', 17.99],
                    ['skirt_196543', 12.99],
                    ['jacket_976535', 26.99],
                    ['pants_086367', 30.99],
                    ['dress_357896', 29.99],
                    ['shoes_157895', 14.99]]

# Write your code below!
#The final addition to our clothes store app will be some logic for bundling overstocked items into groups to sell at once. We would like to split our items by price and then pick three cheaper items and two more expensive items per bundle. Finally, we are going to promote the bundles which have a value greater than 100 dollars.
#For the first step, import the deque and namedtuple classes from the collections module and create a new deque called split_prices.
from collections import *
split_prices = deque()

#Now that the deque has been created, for every clothes item in the overstock_items list, if the price if greater than 20 dollars than append the item to the front of split_prices, otherwise append it to the back of split_prices.
for item in overstock_items:
  if item[1] > 20:
    split_prices.appendleft(item)
  else:
    split_prices.append(item)
print(split_prices)

#To make the data easier to read and work with, create a namedtuple subclass called ClothesBundle. Set the typename to ClothesBundle and the field_names to bundle_items and bundle_price.
ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])

#this next step is a bit tricky. First, create an empty list called bundles. Use a loop to continue iterating as long as there are at least 5 elements left in split_prices.
#On each iteration, append a new ClothesBundle object to the bundles list. The ClothesBundle object will be created by making a bundle of three cheap items and two expensive items. This can be accomplished using list of items by popping from the back of split_prices three times and the popping from the front of split_prices two times.
#Use that list of clothes items as the bundle_items in theClothesBundle. Calculate the sum of the prices for the bundle and store that as the bundle_price in the ClothesBundle.
bundles = []
while len(split_prices) >= 5:
  bundle_list = [split_prices.pop(), split_prices.pop(), split_prices.pop(), split_prices.popleft(), split_prices.popleft()]
  calc_price = sum(b[1] for b in bundle_list)
  bundles.append(ClothesBundle(bundle_list, calc_price))

#Use the bundles list to find out which bundles should be promoted. Create a new list called promoted_bundles. For every bundle in bundles which has a total value of over 100 dollars, add that bundle to promoted_bundles.
promoted_bundles = []
for bundle in bundles:
  if bundle.bundle_price > 100:
    promoted_bundles.append(bundle)

print(promoted_bundles)


























