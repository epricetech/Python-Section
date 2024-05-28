# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:31:51 2023

@author: geron
"""

# Iterable is an object that is capable of being looped through one element at a time.  We commonly use iterables to 
# iterate through sets of data.  Dictionaries, lists, tuples and sets are all iterables
#  Process of iteration is using the for loops.  
# example of dictionary being the iterable and the for loop being the iteration
dog_foods = {
    "Great Dane Foods": 4,
    "Min Pin Pup Foods": 10,
    "Pawsome Pups Foods": 8
}
for food_brand in dog_foods:
    print(food_brand + " has " + str(dog_foods[food_brand]) + " bags")


# iterator objects - __iter__() and iter()
#  above in our for loop the first step is to convert the dictionary (the iterable) to an iterator object
#  an interator object is a special object that represents the stream of data we can operate on.  To do so
# there is a build in function called iter()
dog_food_iterator = iter(dog_foods)
print(dog_food_iterator)
# output of the iter() function
# <dict_keyiterator object at 0x....> 
# # Note: The memory address is omitted since it varies on the system you run the script on. 
# To go behind the scenes even further, iter(dog_foods) is actually calling a method defined within the iterable 
# called __iter__(). All iterables have this __iter__() method defined. We can even use the Python built-in 
# function dir() to show that our dog_foods dictionary (iterable) has a defined method called __iter__().
print(dir(dog_foods))
# output of the dir print statement will show that there is a __iter__ property along with others
# In summary, the __iter__() method simply returns the iterator object that allows us to iterate over the iterable. 
# Calling dog_foods.__iter__() will retrieve the same iterator object as calling iter(dog_foods). This means that 
# the built-in function iter() and the iterable’s method __iter__() can be used interchangeably.

# example of both methods being used
sku_list = [7046538, 8289407, 9056375, 2308597]

# Write your code below:
print(dir(sku_list))

sku_iterator_object_one = sku_list.__iter__()
print(sku_iterator_object_one)

sku_iterator_object_two = iter(sku_list)
print(sku_iterator_object_two)
# output
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# <list_iterator object at 0x7fb087d91fd0>
# <list_iterator object at 0x7fb087eaa4e0>


# iterator objects - __next__() and next()
# this is the next step after we have created our iterator objects.
#  How does the for loop know which value to retrieve on each iteration.  The iterator object has a method
#  called __next__() wich retrieves the itereators next value
# example 
sku_list = [7046538, 8289407, 9056375, 2308597]
sku_iterator = iter(sku_list)
next_sku = sku_iterator.__next__()
print(next_sku)
# output
#7046538
# similair to the iter() function there is alos the next() function
# example of the next() function
sku_list = [7046538, 8289407, 9056375, 2308597]
sku_iterator = iter(sku_list)
next_sku = next(sku_iterator)
print(next_sku)
# output
# 7046538

# now how does the iterator know when to stop the iteration.  The __next__() method will raise an excaeption
# called StopIteration when all items have been iterated thought.  
#  Example of the __next__() method and and iterate thgouth 5 times and the traceback shows the StopIteration exception
sku_list = [7046538, 8289407, 9056375, 2308597]
sku_iterator = iter(sku_list)
for i in range(5):
  next_sku = sku_iterator.__next__()
  print(next_sku)
#output
# 7046538
# 8289407
# 9056375
# 2308597
# Traceback (most recent call last):
#   File "main.py", line 24, in <module>
#     next_sku = sku_iterator.__next__()
# StopIteration


# another example
dog_foods = {
  "Great Dane Foods": 4,
  "Min Pip Pup Foods": 10,
  "Pawsome Pup Foods": 8
}

# Write your code below:
dog_food_iterator = iter(dog_foods)
next_dog_food1 = next(dog_food_iterator)
print(next_dog_food1)
next_dog_food2 = dog_food_iterator.__next__()
next_dog_food3 = dog_food_iterator.__next__()
print(next_dog_food1)
print(next_dog_food2)
next(dog_food_iterator)
# output
# Great Dane Foods
# Great Dane Foods
# Min Pip Pup Foods
# Traceback (most recent call last):
#   File "script.py", line 15, in <module>
#     next(dog_food_iterator)
# StopIteration


# iterators and For loops
# example of putting everything together.  The iterators, the for loop and iteration
dog_foods = {
  "Great Dane Foods": 4,
  "Min Pip Pup Foods": 10,
  "Pawsome Pup Foods": 8
}
for food_brand in dog_foods:
  print (food_brand + " has " + str(dog_foods[food_brand]) + " bags")

# To summarize, the three main steps are:

# The for loop will first retrieve an iterator object for the dog_foods dictionary using iter().

# Then, next() is called on each iteration of the for loop to retrieve the next value. This value is set to
#  the for loop’s variable, food_brand.

# On each for loop iteration, the print statement is executed, until finally, the for loop executes a 
# call to next() that raises the StopIteration exception. The for loop then exits and is finished iterating.


# Customer Iterators
# We have seen that the methods __iter__() and __next__() must be implemented for an object to be an iterator object. 
# The implementation of these methods is known as the iterator protocol.
# If we desire to create our own custom iterator class, we must implement the iterator protocol, 
# meaning we need to have a class that defines at minimum the __iter__() and __next__() methods.
# example - fish story got new fish no classes to manage inventory if we want to track we create custom class initializer
class FishInventory:
  def __init__(self, fishList):
      self.available_fish = fishList
#  by default custom classes are not iterable meaning we cant just plug them into for loops.  To be able to this class
# iterable we must define __iter__() and __next__() methods

# example of this concept of not being able to iterate through defualt classes with for loop without iter and next nethod
class FishInventory:
  def __init__(self, fishList):
      self.available_fish = fishList

fish_inventory_cls = FishInventory(["Bubbles", "Finley", "Moby"])
# Your code below
for fish in fish_inventory_cls:
  print(fish)
# output
# Traceback (most recent call last):
#   File "script.py", line 7, in <module>
#     for fish in fish_inventory_cls:
# TypeError: 'FishInventory' object is not iterable

# to itereate over custom class we implement the iterator protocal by defining __iter__() and __next__()
#  The __iter__() must always return the iterator object iteself.  Typicallly by returning self.  It can also
#  include some class memeber initializing
#  The __next__() must either return the next value available or raise the Stop Iteration exception.  It can
# also include any number of operations
# example and breakdown
class FishInventory:
  def __init__(self, fishList):
      self.available_fish = fishList
 
  def __iter__(self):
    self.index = 0
    return self
# we want to see the class iterable.  We first defind the __iter__() method.  We can initialize a class memeber
# within the __iter__() method called index that will hep us track the current position withing the self.available_fish
# the __iter__() method returns itself since this class will be an iterator object.  Now the __iter__() method
# can return other iterator objects, but typically the object itself is returned here by using return self
# Then we define the __next__() method.  In this method we can perform operations like incrementing class
# members or traversing a for loop
def __next__(self):
    fish_status = self.available_fish[self.index] + " is available!"
    self.index += 1
    return fish_status
# we return the next available fish status within a string value and increment our class member index by 1
#  Now this iteratiion over the class object will error out at some point because we fail to check our index value
# agains the length of the self.available_fish list.  We can avoid this by raising the StopIteration exception in our
#  __next__() method - this code below is a correction to the __next__() method above using and if statement to check
def __next__(self):
    if self.index < len(self.available_fish):
      fish_status = self.available_fish[self.index] + " is available!"
      self.index += 1
      return fish_status
    else:
      raise StopIteration

# example and instructions from start to finish to set up iter and next method with if statement and for loop
class CustomerCounter:
# Write your code below:
  def __iter__(self):
    self.count = 0
    return self
# Next, define the __next__() method. Only 1 customer will enter at a time each time this __next__() method is called.
#If we were to iterate through the customer_counter object using a for loop now, we would get an infinite loop since our __next__() method has not raised a StopIteration exception.Let’s fix this by moving on to Step 5 where we can raise this exception and prevent an infinite loop from occurring! Checkpoint 5 Passed 5.Modify the __next__() method to raise a StopIteration exception when our customer count is greater than 100.
  def __next__(self):
    self.count +=1 
    # Checkpoint 4 & 5
    if self.count > 100:
      raise StopIteration
    return self.count
      
# Create a class instance customer_counter from the CustomerCounter class.
customer_counter = CustomerCounter()
#Create a for loop to iterate through our CustomerCounter class object customer_counter. Print out each customer count value on each loop iteration.
for customer_count in customer_counter:
  print(customer_count)



# Python Itertools - Built in Iterators
#  itertools provides the ability to create complex iterator manipulations.  These iterator operations can input
# either a single iterable or combination of them
#  3 categories of itertool iterators
# 1. Infinite Iterators - will repeat an infinite number of times.  They will not raise a StopIteration exception
#  and will require some type of stop condition to exit from - useful when we have unbounded streams of data to process
#  -can use the count(), cycle() repeat() functions
# 2. Input-Dependent Iterators - are terminiated by the input iterable(s) sequence length.  this means that the 
# smalles length iterable parameter of an input-dependent iterator will terminate the iterator - can use the
# chain(), compress(), filterfals() functions - create for working with and modifying existing iterators
# 3. Cominatoric Iterator - are iterators that are conbinational, where mathmatical functions are performed
# on the input iterable(s) - can use product(), permutations(), combinations() functions
# to use the itertool it must be imported
import itertools

# Infinite Iterator - count()
# count() will count from a frist value until we provide some type of stopy condition
# base syntax
# count(start,[step])
# first argument is the value were we start counting from.  The 2nd argument is an optional step that will 
# return current value + step.  The step can be positive, negative, and integer or float number.  Always default to 1 
# example of count() with start and step and break down
import itertools
 
for i in itertools.count(start=0, step=2):
  print(i)
  if i >= 20:
    break
#  we set start to 0 and step at 2 so that we increment +2 on each iteration.  create a stop condition which is 
#  i>= 20 otherwise the loop would continue forever
# example of count() itertools with if statement and break to stop the infintie loop
# have 13.5 lb bags to display on shelf with max weight of 1000.  find how many bags will fit
import itertools
max_capacity = 1000
num_bags = 0
for i in itertools.count(start=13.5,step=13.5):
  if i >= max_capacity:
    break
  num_bags += 1

print(num_bags)
# output 74


# Input-Dependent Iterator - chain()
# an input dependent iterator will terminate based on the length of one or more input values
# chain() takes in one or more iterables and combine them into a single iterator.  
# base syntax
# chain(*iterables)
# the input value is one or more iterables of the same or varying iterable type.  example we could use chain()
# to combine a list and a set into one iterator.  
#  example of combine list containg odd number and a set containing even numbers and breakdown
import itertools
 
odd = [5, 7, 9]
even = {6, 8, 10}
 
all_numbers = itertools.chain(odd, even)
 
for number in all_numbers:
  print(number)
# sets all_njmbers to the iterator returned by the itertool chain()
# uses the list iterable odd and the set iterable even as the agruments to chain()
# implements a for loop using the iterator in all_numbers
# ouput
# 5
# 7
# 9
# 8
# 10
# 6
# example of chain() itertools combineing 3 iterables
import itertools

great_dane_foods = [2439176, 3174521, 3560031]
min_pin_pup_foods = [6821904, 3302083]
pawsome_pup_foods = [9664865]

# Write your code below: 
all_skus_iterator = itertools.chain(great_dane_foods,min_pin_pup_foods,pawsome_pup_foods)

for sku in all_skus_iterator:
  print(sku)
  

# Cominatoric Iterator - combinations()
# combinatoric iterator will perfom a set of statistical or mathematical operations on an input iterable
#combinations() will produce an iterator of tuples that contain combinations of all elements in the imput
# base syntax
# combinations(iterable,r)
# combinations() takes 2 inputs.  First is an iterable and the second is a value r that represents the length
# of each combination tuple.  The return type of combinations() is an iterator that can be used in a for loop or
# can be converted into a iterable using list() or set()
# example of list of even numbers and we want all possible combinations of 2 even numbers - and breakdown
import itertools
even = [2, 4, 6]
even_combinations = list(itertools.combinations(even, 2))
print(even_combinations)
# we create an iterator using combinations() with the list or even numbers as first arument and 2 as the 2nd argument
# set even_combinations equal to a list of the elements in the iterator returned from combinations()
# then print even_combinations - the resulting list of 2 member tups are the cominations of all 3 memembs of even
# ouput
# [(2, 4), (2, 6), (4, 6)]

# example of combinatons - selving unit can hold only 3 collars.  have list of collars of various colors and sozes
#  We want to know the different combinations to display a set of 3 collars.  
import itertools

collars = ["Red-S","Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

# Write your code below: 
collar_combo_iterator = itertools.combinations(collars,3)
for collar in collar_combo_iterator:
  print(collar)
# output
# ('Red-S', 'Red-M', 'Blue-XS')
# ('Red-S', 'Red-M', 'Green-L')
# ('Red-S', 'Red-M', 'Green-XL')
# ('Red-S', 'Red-M', 'Yellow-M')
# ('Red-S', 'Blue-XS', 'Green-L')
# ('Red-S', 'Blue-XS', 'Green-XL')
# ('Red-S', 'Blue-XS', 'Yellow-M')
# ('Red-S', 'Green-L', 'Green-XL')
# ('Red-S', 'Green-L', 'Yellow-M')
# ('Red-S', 'Green-XL', 'Yellow-M')
# ('Red-M', 'Blue-XS', 'Green-L')
# ('Red-M', 'Blue-XS', 'Green-XL')
# ('Red-M', 'Blue-XS', 'Yellow-M')
# ('Red-M', 'Green-L', 'Green-XL')
# ('Red-M', 'Green-L', 'Yellow-M')
# ('Red-M', 'Green-XL', 'Yellow-M')
# ('Blue-XS', 'Green-L', 'Green-XL')
# ('Blue-XS', 'Green-L', 'Yellow-M')
# ('Blue-XS', 'Green-XL', 'Yellow-M')
# ('Green-L', 'Green-XL', 'Yellow-M')


# overall example of iter and next method with itertools combinations
# Write your code below:
import itertools
max_money = 15
options = []
#Create a list iterable that contains tuples of (cat_toy, price). The list should be called cat_toys. The tuple should consist of the cat toy name and price following the values in the table:
cat_toys = [("laser", 1.99), ("scratcher", 10.99), ("fountain", 5.99), ("catnip", 15.99)]
#Using iter(), create an iterator called cat_toy_iterator that retrieves the iterator for cat_toys.
cat_toy_iterator = iter(cat_toys)
#Using four next() statements, print out each value in cat_toy_iterator 
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))

#A customer enters and only has $15 to spend on exactly 2 cat toys. They want to know how many combinations of the available toys they can afford, while only getting 2 of them total. above the commented out for loop, create a combinations() iterator called toy_combos to retrieve all combinations of 2 total toys from the cat_toys list.
toy_combos = itertools.combinations(cat_toys, 2)

#Each iteration of the for loop gives a tuple that is within toy_combos. The variable toy1 represents index 0 of the tuple (the toy name) and cost_of_toy1 represents index 1 of the tuple (the toy cost). We repeat this to store the toy name and price of toy 2 via variables toy2 and cost_of_toy2.After the final line within the for loop, check if the price of cost_of_toy1 and cost_of_toy2 is less than or equal to max_money which is the max $15 the customer has to spend. If it is, add the tuple to the options list.
for combo in toy_combos:
    toy1 = combo[0]
    cost_of_toy1 = toy1[1]
    toy2 = combo[1]
    cost_of_toy2 = toy2[1]
    if cost_of_toy1 + cost_of_toy2 <= max_money:
      options.append(combo)
      
# Checkpoint 7
print(options)
# output
# ('laser', 1.99)
# ('scratcher', 10.99)
# ('fountain', 5.99)
# ('catnip', 15.99)
# [(('laser', 1.99), ('scratcher', 10.99)), (('laser', 1.99), ('fountain', 5.99))]


































