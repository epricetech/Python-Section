# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:37:24 2023

@author: geron
"""


# # instructions
# Generator Functions & Expressions
# 1.
# You are managing your first customer event! You’ve been provided a guestlist of names and their ages that are 
# within the file guest_list.txt.

# Within the file script.py, there is a defined function called read_guestlist() that will read in the guestlist 
# file line by line. This function will separate the name and age values and store them into variables named name 
# and age respectively.

# Modify this function to be a generator function that will yield each read line so that each guest name is yielded
#  each time for the generator.

# Using a for loop, iterate through the generator object that is retrieved by calling the generator function 
# read_guestlist() and print out the first 10 guests on the guestlist.


# Hint
# The following syntax will turn a normal function into a generator function:

# yield value
# 2.
# We’ve printed out our first 10 guests when our phone rings! It’s our customer who has another guest to
#  add to the guestlist.

# She wants to add a guest with the information: "Jane,35". Use one of the three generator methods we have 
# learned to accomplish this.


# Hint
# The send() method will allow us to send the string "Jane,35" to the generator.

# 3.
# We can now finish yielding the rest of the names on the guestlist file to our generator by adding numerous 
# next() calls on the generator object until a StopIteration exception is reached. This can also be accomplished 
# by using a for loop on the generator object to automatically make the appropriate amount of next() calls.


# Hint
# The syntax for calling next() on the generator object is below:

# next(generator_object)
# 4.
# Now that we have all our guests, we want to see which guests are aged 21 and over so that we can inform the 
# bartending vendor.

# Define a generator expression that will use the guests dictionary to retrieve a generator of names of all 
# guests who are 21 and over.

# We should see our newly added guest, Jane on this list as well!


# Hint
# The generator expression should contain an if statement to check the age of the guest.

# Connected Generators & Generator Pipelines
# 5.
# Now it’s time to assign meals to each table and the seats at the tables. Our event will have 3 tables with 5 
# seats at each.

# Create 3 separate generator functions, one for each table, that will yield tuples of 
# ("Food Name", "Table X", "Seat Y") for each of the 5 seats at each table.

# You may use the following foods for the tables: Chicken, Beef, Fish.


# Hint
# The generator function for each table should use the range() function to yield the food name, table number, 
# seat number tuple.

# 6.
# Finally, we want to assign a table and seat number with meal selection to each guest. Create another 
# generator function that will take in as input our guests dictionary and the connected generator 
# seating/food selection we created in the previous step. This function should yield a tuple of the guest name 
# and the next value from the connected generator.


# Hint
# The next() function can be called within the yield statement similar to the following:

# yield (name, next(another_generator))
# Finishing Up
# 7.
# Congratulations, you were able to successfully plan and coordinate your first event!

# Through this project, you were able to reinforce what generators are, how they can be created, manipulated,
#  and connected together to perform complex generator operations.
# Tim,22
# Tonya,45
# Mary,12
# Ann,32
# Beth,20
# Sam,5
# Manny,76
# Kenton,15
# Kenny,27
# Dixie,46
# Mallory,32
# Julian,4
# Edward,71
# Rose,65

guests = {}
def read_guestlist(file_name):
    text_file = open(file_name,'r')
    while True:
        x = yield
        if x is None:
          line_data = text_file.readline().strip().split(",")
        else:
          line_data = x.split(",")
        if len(line_data) < 2:
        # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
        yield name 
                                            
guestlist = read_guestlist('guest_list.txt')

for k in range(20):
  print(next(guestlist))

#Add Jane,35 to the generator
next(guestlist)
guestlist.send("Jane,35")

for k in range(8):
  print(next(guestlist))

def guest_age(guest_dict):
  for key,val in guest_dict.items():
    if val > 21:
      yield key

age_of_guest = guest_age(guests)

for obj in age_of_guest:
  print(obj)

def table_one():
  for j in range(1,2):
    for k in range(1,6):
      yield "Chicken", "Table {}".format(j),"Seat {}".format(k)

def table_two():
  for j in range(2,3):
    for k in range(6,11):
      yield "Beef", "Table {}".format(j), "Seat {}".format(k)

def table_three():
  for j in range(3,4):
    for k in range(11,16):
      yield "Fish", "Table {}".format(j), "Seat {}".format(k)


def combined_tables():
  yield from table_one()
  yield from table_two()
  yield from table_three()

combined_tables = combined_tables()

def guest_assignment():
  for name in guests.keys():
    yield name, next(combined_tables)

guest_assignment = guest_assignment()
for person in guest_assignment:
  print(person)






















