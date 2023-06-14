# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 09:30:05 2023

@author: geron
"""

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



countdown = 10
while countdown >= 0:
  print(countdown)
  countdown -= 1
print('We have liftoff!') 



ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
length = len(ingredients)
index = 0
 
while index < length:
  print(ingredients[index])
  index += 1



python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0
while index < length:
  print('I am learning about ' + python_topics[index])
  index += 1


#this loop keeps gong forever because their is never an end value set - infinate loop
my_favorite_numbers = [4, 8, 15, 16, 42]
 
for number in my_favorite_numbers:
  my_favorite_numbers.append(1)








