# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 09:50:21 2023

@author: geron
"""

# loops - they loop through a variables values till condition is met.  it can be used to iterate over a list of items
# and perform various action on each item.  
# for loop syntax
# for <temporary variable> in <list
# variable>:
# <action statement>
# <action statement>
# 

# You can use the break or continue function to end or continue loop
# break - Terminates the current loop and resumes execution of the next statement.  usually paired with if elif else statements
# syntax for break for and while loops
for letter in 'Python':     # First Example
    if letter == 'h':
        break
    print('Current Letter :', letter)
  
var = 10                    # Second Example
while var > 0:              
    print('Current variable value :', var)
    var = var -1
    if var == 5:
     		break
print("Good bye!")


#this loop will continue to the end of the list even if it finds the correct data - have to use break to fix
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
for item in items_on_sale:
  if item == "knit dress":
    print("Found it")

# - this one stops when the correct data is found in the list
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
print("Checking the sale list!")
for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break
print("End of search!")

# example of continue control in for loop with if statement
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"
for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print('They have the dog I want!')
    break

# continue - returns the control to the beginning of the loop.  Continue rejects all remaining statements
# Syntax for continue for and while loops
for letter in 'Python':     # First Example
    if letter == 'h':
        continue
    print('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:              
   	var = var -1
   	if var == 5:
           continue
   	print('Current variable value :', var)
print("Good bye!")

# example continue control
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
  if i <= 0:
    continue
  print(i)

#example of continue control
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for i in ages:
  if i < 21:
    continue
  print(i)

# example of continue and break in a single while loop
while True:
    print ('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print ('Hello, Joe. What is thepassword?  (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print ('Access granted.')

  
# infinate loop - a loop that never ends because of the end value set
my_favorite_numbers = [4, 8, 15, 16, 42]
for number in my_favorite_numbers:
  my_favorite_numbers.append(1)

# While loop - will repeatedly execute a code block as long as a condition evaluates to true.  
# the while loop condition is always checked first before block of code runs. 
# if the condition is not met inititally then the code of block will never run
# while loop syntax
# i = 1
# while i < 6:
# print(i)
# i = i + 1
# example simple while loop
count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1

# example from above in a single command
count = 0
while count <= 3: print(count); count += 1

# example while loop - will continune iteration till condition is met
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")


# example of while loop 
countdown = 10
while countdown >= 0:
  print(countdown)
  countdown -= 1
print('We have liftoff!') 

# example while loop with len method - will iteratate through list till it hits length of list
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
length = len(ingredients)
index = 0
while index < length:
  print(ingredients[index])
  index += 1

# example while loop with len method - will go through till it hits end of list
python_topics = ["variables", "control flow", "loops", "modules", "classes"]
length = len(python_topics)
index = 0
while index < length:
  print('I am learning about ' + python_topics[index])
  index += 1

# example of while loop - will go through each iterattion and print out what the count is currently till it reaches
# the while statement
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")

# example while loop will count down till it reaches while statement
countdown = 10
while countdown >= 0:
  print(countdown)
  countdown -= 1
print('We have liftoff!') 

# example while loop that uses len to get count of list
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
length = len(ingredients)
index = 0
while index < length:
  print(ingredients[index])
  index += 1
  
# example while loop that goes through a list and prints a statement for each value
python_topics = ["variables", "control flow", "loops", "modules", "classes"]
length = len(python_topics)
index = 0
while index < length:
  print('I am learning about ' + python_topics[index])
  index += 1

# example of function with for loop and if statement
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count
print(divisible_by_ten([20, 25, 30, 35, 40]))

# appends a list and creates a new one
def add_greetings(names):
  empty = []
  for name in names:
    empty.append('Hello, ' + name)
  return empty
print(add_greetings(["Owen", "Max", "Sophie"]))


# deleting the starting numbers to get to an odd one
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


# find the odd values in a list
def odd_indices(lst):
  new_list = []
  for index in range(1, len(lst), 2):
    new_list.append(lst[index])
  return new_list
print(odd_indices([4, 3, 7, 10, 11, -2]))

# nested loops - loops inside of other loops.  nested loops can be used to access items of lists which are inside
# other lists.  the item selected from the outer loop can be used as the list for the inner loop it iterate over

groups = [["Jobs", "Gates"], ["Newton",
"Euclid"], ["Einstein", "Feynman"]]
# This outer loop will iterate over each list in the groups list
for group in groups:
# This inner loop will go through each name in each list
    for name in group:
        print(name)


# example nested loops
def exponents(bases, powers):
  new_exponents = []
  for base in bases:
    for power in powers:
      new_exponents.append(base ** power)
  return new_exponents

print(exponents([2, 3, 4], [1, 2, 3]))

# example of nested loops
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

for team in project_teams:
  print(team)
# Loop through each sublist - nested loop
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)
    
# example of nested loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element

print(scoops_sold)

# for loops with range . this can be used to perform an action a specific number of times in a row.  Can be used
# to create a list that can be used to specify the number of iterations in a for loop
# For loop with i in range
#must contain the for keyword a variable name the in keyword a call to range() up to 3 integers
# a colon and a clause and indented block of code
#can also use continue and break statemes inside of for loops and while loops

# Print the numbers 0, 1, 2:
for i in range(3):
    print(i)
# Print "WARNING" 3 times:
for i in range(3):
    print("WARNING")

#examples of for loop with i range - 
#starting  and starting  arguments  pick where the numbers begin and end
for i in range (12, 16):
    print (i)

#Steping arguments
for i in range (0, 10, 2):
    print (i)

# negagtime stepping
for i in range (5, -1, -1):
    print(i)
# example of for loop with range
print ('My name is ')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')


# Gauss formula to figure out the answer to if you add up all the numbers from 0 to 100
total = 0
for num in range(101):
    total = total + num
print(total)

single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
for i in single_digits:
  print(i)
  squares.append(i**2)
print(squares)
# Example of above coe but in a single line
cubes = [num ** 3 for num in single_digits]
print(cubes)

#example - simple loop with range incements the temp variable by one on each loop
for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))

# example - simple loop with range 
promise = "I will finish the python loops module!"
for temp in range(5):
  print(promise)

# Function with 2 loops and if statment - finding the larger sum in the 2 lists
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

#example of function with for statment and if statement
def over_nine_thousand(lst):
  sum = 0
  for num in lst:
    sum += num
    if (sum > 9000):
      break
  return sum
print(over_nine_thousand([8000, 900, 120, 5000]))


#  function with for and if statements find the max number
def max_num(nums):
  max = nums[0]
  for numbers in nums:
    if numbers > max:
      max = numbers
  return max
print(max_num([50, -10, 0, 75, 20]))



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














