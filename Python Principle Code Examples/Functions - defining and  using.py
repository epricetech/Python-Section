# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 09:09:09 2023

@author: geron
"""
#Structure: to create a function
#def function_name: 
   # function definition statements...
# or
# def function_name(paramater1, parameter2 ect):
        # function statements(arguments)
# functions can also include arguments when they are called
# syntax     function_name('argument1', 'argument2')
# there are 3 different types of arguments for a function
# 1. Positional argument - arguments that can be called by their position in the function definition - the index value
# 2. Keyword argument - argument that can be called by their name in the function paramaters
# 3 - defualt argument - arguments that are given defualt values in the function definition
# example of creating a function and calling it.  this is order specific.  
def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')
def c():
    print('c() starts')
    print('c() returns')
def d():
    print('d() starts')
    print('d() returns')

a()
#output
# a() starts
# b() starts
# c() starts
# c() returns
# b() returns
# d() starts
# d() returns
# a() returns


# example of creating a function and then putting in print statements and calling the function
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
# these print jobs wont run because they are inside the function.  need to call the function to run the print that are inside
directions_to_timesSq()


# in this example a print statement is outside of function.  It will run that first and then the function call will run
# it runs this way based on order
def trip_welcome():
  # Indented code is part of the function body
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")
 
# Unindented code below is not part of the function body
print("Woah, look at the weather outside! Don't walk, take the train!")
 
trip_welcome()

# functions with parameter
# calling each function with an default argument
# def my_function(single_parameter) - defines a single parameter
    
def trip_welcome(destination):
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to " + destination + " today.")
trip_welcome("Times Square")
  


def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)

generate_trip_instructions("Grand Central Station")


# function with statements and calling the function using defualt arguments
# Write your tenth_power function here:
def tenth_power(num):
  num = num ** 10
  return num
# or just return num ** 10
# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

# example   find the square root
# square root

# Write your square_root function here:
def square_root(num):
  return num ** 0.5
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10


# function with multiple parameters and returning a specific statement when function is called
def win_percentage(wins, losses):
  return (wins / (wins + losses) * 100)
  
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100


# function to find the average 
# Write your average function here:
def average(num1, num2):
  sum = num1 + num2
  sum = sum / 2
  return sum
# or can do it   return(num1 + num2) / 2
# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0


# remainder
# the % returns the remainder of one number divided by another
# Write your remainder function here:
def remainder(num1, num2):
  sum1 = num1 * 2
  sum2 = num2 / 2
  return sum1 % sum2
# or return (2 * num1) % (num2 / 2)
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0


# tip calc example function

# Write your tip function here:
def tip(total, percentage):
  return (total * percentage) / 100
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0



# bond james bond string function uses a return and defualt paramaters
# Write your introduction function here:
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou


# functin with a lot of statements and math
# all operations

def lots_of_math(a, b, c, d):
  res1 = a + b
  res2 = c - d
  print(res1)
  print(res2)
  res3 = res1 * res2
  print(res3)
  return res3 % a
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0


# function for temperature converstion.  no print our output statements
# Write your code below: 
def f_to_c(f_temp):
  cel = (f_temp - 32) * 5/9 
  return cel
# you can also write it as return (f_temp - 32) * 5/9

f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = (c_temp * 9/5) + 32
  return f_temp

c0_in_farenheit = c_to_f(0)


# function example with multiple functions being used and called

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c=3*10**8):
  return mass * c**2
bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

def get_work(mass, acceleration, distance):
  force = get_force(mass,acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " Meters.")

#output
# The GE train supplies 226800 Newtons of force.
# A 1kg bomb supplies 90000000000000000 Joules
# The GE train does 22680000 Joules of work over 100 Meters.

# function that sets up a welcome message and creates a function for estimated travel time
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)
trip_planner_welcome("Eric")
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time
# sets the argument for the funciton
estimate = estimated_time_rounded(2.5)
#this function has multiple parameters and one that is pre-set
def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")
# this sets the arguments for the function
destination_setup("New York", "London", estimate, "Plane")

# function with multiple paramaters.  if statement where ** means raised to the power of another so here base to the 
# power of exponent
def large_power(base, exponent):
  if base ** exponent > 5000: 
    return True
  else:
    return False
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

#output for both
# Welcome to tripplanner v1.0 Eric
# Your trip starts off in New York
# And you are traveling to London
# You will be traveling by Plane
# It will take approximately 2 hours
# True
# False

# function that takes a list and index locaitons for calling function
weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']
 
def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day


monday, tuesday, wednesday = threeday_weather_report(weather_data)
 
print(monday)
print(tuesday)
print(wednesday)

# there is an error in this one that wont let it print.  I think it is somehwere in the indentaton
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third
  most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()
  print(most_popular1)
  print(most_popular2)
  print(most_popular3)
  

# function with 2 parameters and calling function with default arguments
def trip_welcome(origin, destination):
  print("Welcome to Tripcademy")
  print("Looks like you are traveling from " + origin)
  print("And you are heading to " + destination)
# this is how you call multiple parameters
trip_welcome("Prospect Park", "Atlantic Terminal")


# function with multiple paramaters and statements
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  print(car_rental_total + hotel_total + plane_ticket_price)
calculate_expenses(200, 100, 100, 5)


# this is an example of positional arguments
def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )
calculate_taxi_price(100, 10, 5)

# example of a keyword argument
calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)

# example of default arugment
def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )
# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)
 
# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)


#  example of all 3 of them in use
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")
trip_planner
trip_planner("Brooklyn", "Queens")


#output
# Welcome to Tripcademy
# Looks like you are traveling from Prospect Park
# And you are heading to Atlantic Terminal
# 1190
# 995
# 40.0
# -5.0
# -15.0
# Here is what your trip will look like!
# First, we will stop in France, then Germany, and lastly Denmark
# Here is what your trip will look like!
# First, we will stop in Denmark, then France, and lastly Germany
# Here is what your trip will look like!
# First, we will stop in Iceland, then India, and lastly Germany
# Here is what your trip will look like!
# First, we will stop in Brooklyn, then Queens, and lastly Codecademy HQ


# function example with if and elif statements also using random number generator - Magic 8 ball
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is Certain'
    elif answerNumber == 2:
        return ' It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'No'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Still hazy'
    elif answerNumber == 7:
        return 'Outlook is not good'
    elif answerNumber == 8:
        return 'You can forget about it'
    elif answerNumber == 9:
        return 'Only god knows'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

# can simplify last 3 lines by passing return values as an argument to another function call
print(getAnswer(random.randint(1,9)))


# example - function with for loop with range
def testfunction(number):
# This code is part of testfunction
    print("Inside the testfunction")
    sum = 0
    for x in range(number):
# More indentation because 'for' has a code block but still part of he function
        sum += x
        return sum
print("This is not part of test function")


# example function with multiple arguments and different ways of calling function
def findvolume(length=1, width=1,depth=1):
    print("Length = " + str(length))
    print("Width = " + str(width))
    print("Depth = " + str(depth))
    return length * width * depth;

findvolume(1, 2, 3)
findvolume(length=5, depth=2, width=4)
findvolume(2, depth=3, width=4)


# example function with multiple parameters and returning  multiple values
def square_point(x, y, z):
    x_squared = x * x
    y_squared = y * y
    z_squared = z * z
# Return all three values:
    return x_squared, y_squared, z_squared
three_squared, four_squared, five_squared = square_point(3, 4, 5)


# example of function that sorts a list
def combine_sort(my_list1, my_list2):
  unsorted = my_list1 + my_list2
  sortedList = sorted(unsorted)
  return sortedList

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


# function with if statement and list
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# function with if statement and lists
def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  else:
    return my_list2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# example of function with list appends
def append_sum(my_list):
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  return my_list

print(append_sum([1, 1, 2]))

#example function that uses range and list method
def every_three_nums(start):
  nums = range(start, 101, 3)
  return list(nums)
# can also be written 
# return list(range(start, 101, 3))

print(every_three_nums(91))

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

# example function with for loop and if statement
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

# appends a list and creates a new one
def add_greetings(names):
  empty = []
  for name in names:
    empty.append('Hello, ' + name)
  return empty

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))


# deleting the starting numbers to get to an odd one
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


# find the odd values in a list
def odd_indices(lst):
  new_list = []
  for index in range(1, len(lst), 2):
    new_list.append(lst[index])
  return new_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

# Example functino with 2 loops and if statement - finding the larger sum in the 2 lists
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for num1 in lst1:
    sum1 += num1
  for num2 in lst2:
      sum2 += num2
  if sum1 >= sum2:
    return lst1
  else:
    return lst2
print(larger_sum([1, 9, 5], [2, 3, 7]))

# example function with for loop and if statement
def over_nine_thousand(lst):
  sum = 0
  for num in lst:
    sum += num
    if (sum > 9000):
      break
  return sum
print(over_nine_thousand([8000, 900, 120, 5000]))


#  Function with for and if statements find the max number
def max_num(nums):
  max = nums[0]
  for numbers in nums:
    if numbers > max:
      max = numbers
  return max
print(max_num([50, -10, 0, 75, 20]))

# Function with for range and if statment with append - finding the same values
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))



# Function with for range statement with if statement reversed list matching
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))


def print_each_letter(word):
  for letter in word:
    print(letter)

favorite_color = "blue"
print_each_letter(favorite_color)
# => 'b'
# => 'l'
# => 'u'
# => 'e'


def get_length(word):
  counter = 0
  for letter in word:
    counter += 1
  return counter

# will check the 2 elements in function for matching letters
def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

# exanoke if function with for and if statements and working with strings
# will only print characters with even index
def print_some_characters(word):
  for i in range(len(word)):
    if i % 2 == 0:
      print(word[i])
print_some_characters("watermelon")


# example of formating strings with variables
# - to include variables in strings uses {}
def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)
print(favorite_song_statement("Smooth", "Santana"))
# => "My favorite song is Smooth by Santana."
def poem_title_card(title, poet):
  poem_desc = "The poem \"{}\" is written by {}.".format(title, poet)
  return poem_desc
def favorite_song_statement(song, artist):
  return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)
def favorite_song_statement(song, artist):
  # this will have the same output as the above example
  return "My favorite song is {song} by {artist}.".format(artist=artist, song=song)
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc
author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"
my_beard_description = poem_description(publishing_date, author, title, original_work)
print(my_beard_description)

# example function showing how global variables and those inside function
# when you use variables the difference between global variables and those inside functions
favorite_locations = "Paris, Norway, Iceland"
def print_count_locations():
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)
print_count_locations()
show_favorite_locations()
current_budget = 3500.75
def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))
print_remaining_budget(current_budget)
def deduct_expense(budget, expense):
  return(budget - expense)
shirt_expense = 9
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)
print_remaining_budget(new_budget_after_shirt)


# example function with for loop with value() function amd isomg dictionary
def sum_values(my_dictionary):
  sum = 0
  for value in my_dictionary.values():
    sum += value
  return sum
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6


# example function with for loop and if statment and using .keys() method
def sum_even_keys(my_dictionary):
  sum = 0
  for value in my_dictionary.keys():
    if value % 2 == 0:
      sum += my_dictionary[value]
  return sum
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6


# example function just like above - to dictionary
def add_ten(my_dictionary):
 for key in my_dictionary.keys():
    my_dictionary[key] += 10
 return my_dictionary
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# another example of function for and if statements and dictionary
# Write your max_key function here:
def max_key(my_dictionary):
  largest_key = float('-inf')
  largest_value = float('-inf')
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"


# Write your word_length_dictionary function here:  word length dictionary
def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}


# Write your frequency_dictionary function here:  - frequency count
def frequency_dictionary(words):
  frequency = {}
  for word in words:
    if word not in frequency:
      frequency[word] = 0
    frequency[word] += 1
  return frequency
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}


# Write your unique_values function here:  unique values
def unique_values(my_dictionary):
  unique = []
  for word in my_dictionary.values():
    if word not in unique:
      unique.append(word)
  return len(unique)
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1


# Write your count_first_letter function here:  count first letter
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}


# example function with for and if loop
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  unique = 0
  for letter in letters:
    if letter in word:
      unique += 1
  return unique
print(unique_english_letters('mississippi'))
print(unique_english_letters('Apple'))


#example of function with for and if loop
# Write your count_char_x function here:
def count_char_x(word, x):
  occurences = 0
  for letter in word:
    if letter == x:
      occurences += 1
  return occurences
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# example funcaiton with len and split function
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1


# example function using find method on strings
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
    return(word[start_ind + 1: end_ind])
  return word
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


# example function with if len and for and split
# Write your x_length_words function here:
def x_length_words(sentence, x):
  words = sentence.split(' ')
  for word in words:
    if len(word) < x:
      return False
  return True
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

# example function with title method and if statement
def check_for_name(sentence, name):
  sentence = sentence.title()
  name = name.title()
  if name in sentence:
    return True
  else:
    return False
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# example like above but writen differently
# or you can write it like this
def check_for_names(sentence, name):
    return name.title() in sentence.title()
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False


# example function with for in range loop and len method
# Write your every_other_letter function here:  doesnt give correct results
def every_other_letter(word):
  every_other = ''
  for letter in range(0, len(word), 2):
    every_other += word[letter]
  return every_other
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 


# function with for in range but going in revers
# Write your reverse_string function here: doesnt display correctly
def reverse_string(word):
  every_other_reverse = ''
  for letter in range(len(word)-1, -1, -1):
    every_other_reverse += word[letter]
  return every_other_reverse
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print


# function calling using index
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  return word2[0] + word1[1:] + ' ' + word1[0] + word2[1:]

print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


# example function with while loop
# Write your add_exclamation function here:
def add_exclamation(word):
  while len(word) < 20:
    word += '!'
  return word
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn


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








