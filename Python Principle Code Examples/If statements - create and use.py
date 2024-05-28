# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:35:42 2023

@author: geron
"""

# used to check conditions and  depending on true or false will continue to the next line
# syntax
# if condition:
    #body of if statment
#Example:
number = 10

# check if number is greater than 0
if number > 0:
    print('Number is positive.')

    print('The if statement is easy')

#example - 2 different if statements
user_name = "Dave"
if user_name == "Dave":
  print("Get off my computer Dave!")
user_name = "angela_catlady_87"  
if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")    
 
#Example - 2 if statement with 2 requirements and using an or and and clause
credits = 118
gpa = 2.0
if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")
  
credits = 120
gpa = 2.0
if credits >= 120 and gpa >= 2.0:
  print("You have met all of the requirements.")

# example - if not statments - checks each statement and sees if condition is met or not
# not operator returns true if the statement is not true and false if the statement is true
credits = 118
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")
if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")
if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")


   
# If - Else
# 	Used to check conditions and then gives options for output.  Blocks.py
# Structure:
# 	if expression:
#    	statement(s)
# else:
#    	statement(s)

#Example: if else statement with an input
name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print ('Hello, Mary' + ' what is your password? ')
    password = input()
    if password == 'swordfish':
        print ('Access granted')
    else:
        print ('Wrong password.')


# IF - Elif
# 	Used to compare multiple conditions and then output.  blocks.py
# Structure:
# 	if expression1:
#    		statement(s)
# elif expression2:
#    		statement(s)
# elif expression3:
#    		statement(s)
# else:
#  		  statement(s)

#Example: if elif statment 
name = 'Carol'
age = 3000
if name == 'Alice':
    		print ('Hello Alice')
elif age < 12:
    		print ('You are not Alice, kiddo.')
elif age > 2000:
   		 print ('Unlike you, Alice is not an undead, importal vampire.')
elif age > 100:
    		print ('You are not alice, Grannie')
            
# example if elif statement
grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")            
            

# example of if elif statement with conditions and using random number generator 
import random
planet = random.randint(0,6)
weight = 100
if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19
 
print("Your weight:", weight)


# example if elif statements - magic 8 ball - print section is not the cleanest but will run
name = input("What is your name")
question = input("What is your question")
answer = ""
import random
random_number = random.randint(1,12)
print(random_number)
if random_number == 1:
  answer = "Yes Definitely"
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
   answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Who do you think I am."
elif random_number == 11:
  answer = "All lines are busy please try again."
elif random_number == 12:
  answer = "I can't lie to you."
else:
  answer = "Error"
if name == "":
  print("Question "+ question)
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)
if question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something")
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

# example of if and elif and else statments
weight = 41.5

#ground shipping
if weight <= 2:
    ship_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
    ship_ground = weight * 3.0 + 20
elif weight > 6 and weight <= 10:
    ship_ground = weight * 4.0 + 20
else:
    ship_ground = weight * 4.75 + 20
ship_premium = 125
print("Ground Shipping Premium $", ship_premium)
#Drone Shipping
if weight <= 2:
    ship_drone = weight * 4.5
elif weight > 2 and weight <= 6:
    ship_drone = weight * 9.0
elif weight > 6 and weight <= 10:
    ship_drone = weight * 12.0
else:
    ship_drone = weight * 14.25
print(ship_ground)
print(ship_drone)


# example of function with for and if statement
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))


#examples of functions with for and if statements
def over_nine_thousand(lst):
  sum = 0
  for num in lst:
    sum += num
    if (sum > 9000):
      break
  return sum


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))


#  find the max number
def max_num(nums):
  max = nums[0]
  for numbers in nums:
    if numbers > max:
      max = numbers
  return max

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))



# finding the same values

#Write your function here
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))



# reversed list matching

#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

# example of if and else statement - these are called blocks
name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print ('Hello, Mary' + ' what is your password? ')
    password = input()
    if password == 'swordfish':
        print ('Access granted')
    else:
        print ('Wrong password.')

  # will print out the unlike you statement    if you switch 2000 and 100 order it will output you are not alice grannie elif goes in order till first true
name = 'Carol'
age = 3000
if name == 'Alice':
    print ('Hello Alice')
elif age < 12:
    print ('You are not Alice, kiddo.')
elif age > 2000:
    print ('Unlike you, Alice is not an undead, importal vampire.')
elif age > 100:
    print ('You are not alice, Grannie')
else: 
    print('You are way old')






