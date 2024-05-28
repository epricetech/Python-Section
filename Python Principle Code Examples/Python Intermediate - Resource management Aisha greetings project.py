# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 10:13:42 2023

@author: geron
"""

# Aisha, the owner of Aisha’s Greetings, wants to create a program that will automatically generate pre-filled orders, 
# using her custom greeting messages. Use your knowledge of context managers to accomplish this goal!

# First, import the contextlib modules @contextmanager decorator, and create a decorated function named generic that 
# takes in card type, sender’s name, and recipient arguments.


# Hint
# To import a built-in module, we can use the following syntax:

# from <module> import <specific part of module>
# In our case, we want to import the @contextmanager decorator so that way we can decorate a function to become a 
# context manager. Here is how we decorate a function:

# @decorator
# def function_name(): 
# 2.
# The generic() function will serve the purpose of opening a specific generic card type (Thank you card or Birthday card)
#  so that it can be used as the base template for a more customized card.

# Inside the function create the following:

# A variable to store a call of the open() built-in function that opens up a generic card type based on the card 
# type parameter in read mode. You can assume the store will receive either a birthday card request or a thank you 
# card request.

# A variable to store a call of the open() built-in function that creates (and opens) a new card named with the 
# following pattern: < sender_name >_generic.txt.

# Use the sender name parameter from the function definition. Open the file in write mode since we will need to 
# write a new card to the file.


# Hint
# Use an “f” string method to incorporate the sender name into the file!

# some_variable = 'xyz'
# open(f"{some_variable}_file_name.txt", 'w')
# Here we would produce a file named 'xyz_file_name.txt'

# 3.
# Now, you need to make sure the context manager correctly creates a customized card from the generic template.
#  Inside the generic() context manager use the try clause to yield a file so that it creates the following template 
#  custom card:

# Dear < receiver >
# < text from the generic template card > 
# Sincerely, < sender >
# Make sure to use '\n' to create line breaks!


# Hint
# Here, you will need to use the new generic card we created in the last step as well as the template card. 
# Remember, you saved both to a variable and can use them in the try clause. There are three steps involved here:

# A call using the built-in function write() to create "Dear < receiver >". We can use the receiver from our generic() 
# functions definition.

# A call using the built-in function write() to create "< text from the generic template card >". 
# Here we will need to capture the text from the generic card using the built-in function read().

# A call using the built-in function write() to create "Sincerely, < sender >". We can use the sender 
# from our generic() function definition.

# Don’t forget to lastly, yield the file you are working on, otherwise it won’t work with the with statement.

# 4.
# Finally, make sure to close both files after usage!


# Hint
# Use the finally clause to make sure files are closed after use. Make sure to close both the new file and the 
# template file!

# 5.
# It’s time for a test run! Aisha’s Greetings just got a customer ‘Mwenda’ who requested an order for a
#  generic Thank you card for her friend ‘Amanda’.

# Use a with statement to generate this order. Have the with statement confirm the card is created
#  by printing 'Card Generated!'.


# Hint
# Here is how we can call a with statement with a decorator-based context manager:

# with decorator_context_manager(arg1, arg2) as file:
#   print('Some message')
# 6.
# We want to verify whether or not the correct order was printed in the file. Use a with statement to open
#  and read the file you just created in the last step.


# Hint
# Your code should look something like this:

# with open("name_generic.txt", "r") as first_order:
#  print(first_order.read())
# Setting Up Personalized Greeting Cards
# 7.
# Aisha’s Greetings also wants to print personalized cards! This means that customers can tell Aisha’s
#  Greetings the words they want in their card and we can print them.

# For personalized cards, let’s create a class-based context manager. First, create a class called personalized.


# Hint
# You create a class like this: class < CapWordsClass >:

# 8.
# Next, write a __init__ method that takes the sender’s and receiver’s names and saves them as attributes.

# Add one more attribute that stores a newly opened (or created) file in write mode with the 
# format < sender_name >_personalized.txt. This is the file we will be working on!


# Hint
# Remember, to create a class attribute we must preface the name with self.. Here is an example 
# of a __init__ method that creates an attribute from the methods defined parameter:

#  def __init__(self, param1):
#    self.attribute = param1
# 9.
# Now, let’s set up what should happen when any new files are created and the context is started.

# Make an __enter__ method that writes the receiver’s name to the opened file and returns that file. 
# The format we write to the file should look like this: Dear < receiver>


# Hint
# The base syntax could look like this:

#  def __enter__(self):
#    # some operation...
#    return self.file
# 10.
# Lastly, let’s set up the final pieces of the customized card.

# Create an __exit__ method that writes "Sincerely" followed by the sender’s name on the open file and
#  then closes the file!


# Hint
# Your code should look something like this:

#  def __exit__(self, exc_type, exc_value, Traceback):
#    # some operation...
#    self.file.close()
# 11.
# Time to give our custom card generator a test run!

# Aisha’s shop just got a customer 'John' who requested an order for a personalized card for his close friend 'Michael'.

# John wants the body of the letter to say "I am so proud of you! Being your friend for all these years 
# has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire
#  me and I love you! All the best. Always."

# Use the context manager with a with statement to generate this order.


# Hint
# Your code should look something like this:

# with personalized( < arguments > ) as card:
#  card.write( < message > )
# Aisha’s Greetings: Picking up speed!
# 12.
# Aisha’s Greetings just got two orders from a customer named 'Josiah'.

# He wants to get a generic birthday card for a colleague named 'Remy' and a personalized card for his 
# sister 'Esther' that says:

# "Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain 
# I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! 
# You’re getting old!“

# Create a nested with statement that generates these orders in one call.


# Hint
# A with statement can be nested in two ways:

# with ContextManagerA() as A, ContextManagerB() as B:
#   # code here....
# with ContextManagerA() as A:
#   with ContextManagerB() as B:
#     # code here....
# 13.
# Congrats! You were able to help Aisha’s Greetings create a system that generates cards quicker and smoother 
# using the knowledge you gained about context managers!

# Take some time to check out the great cards you created!

# Generic Card

from contextlib import contextmanager

@contextmanager
def generic(card_type, sender, receiver):
  card_file = open(card_type, 'r')
  order = open(f"{sender}_generic.txt", 'w')

  try:
    order.write(f"Dear {receiver}, \n")
    order.write(card_file.read())
    order.write(f"\nSincerely, {sender} \n")
    yield order

  finally:
    card_file.close()
    order.close()

# Uncomment to run!
# with generic("thankyou_card.txt", "Mwenda", "Amanda") as order1:
#   print('Card Generated! \n')

# with open("Mwenda_generic.txt", "r") as first_order:
#   print(first_order.read())


# Personalized Letter
class personalized:
  def __init__(self, sender, receiver):
    self.file = open(f"{sender}_personalized.txt", 'w')
    self.sender = sender
    self.receiver = receiver

  def __enter__(self):
    self.file.write(f"Dear {self.receiver}, \n \n")
    return self.file

  def __exit__(self, exc_type, exc_value, Traceback):
    self.file.write(f"\n \n Sincerely, \n {self.sender}")
    self.file.close()

# Uncomment to run!

# with personalized("John", "Michael") as card:
#  card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")
  
# with generic("happy_bday.txt","Josiah","Remy" ) as card, personalized("Josiah","Esther") as card2:
#   card2.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")