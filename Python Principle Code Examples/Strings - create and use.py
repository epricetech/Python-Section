# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:11:00 2023

@author: geron
"""

# strings - a sequence of characters.  They can be any length and can include any character such as letter, numbers
# symbols and whitespace, spaces, tabs.  and various methods can be used on strings like concat, join, replace, find, strip ect
# you can use \ as escape characters in string
txt = "She said \"Never let go\"."
print(txt) # She said "Never let go".
# escape characters
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""
# bottom one becomes top one with escape characters
password = "theycallme"crazy"91"
password = "theycallme\"crazy\"91"

# you can use in syntax to determine if a ltter or a substring exists in a string.  will return true or false
#example of string with in syntax
game = "Popular Nintendo Game: Mario Kart"
print("l" in game) # Prints: True
print("x" in game) # Prints: False

# can print strings by index
favorite_fruit = "blueberry"
print(favorite_fruit[0])

#  save an element of a string based on index to a variable
my_name = 'Eric'
first_initial = my_name[0]

# grab a chunk of a string based on index
favorite_fruit = "blueberry"
print(favorite_fruit[4:6])

# open selections of a string based on open ended index
print(favorite_fruit[:4])
# Output: blue
print (favorite_fruit[4:])
# Output: berry

# example of string where you pull specific values based on index and assign to new variable
first_name = "Rodrigo"
last_name = "Villanueva"
new_account = last_name[:5]
temp_password = last_name[2:6]
print(new_account + ' ' +  temp_password)

# concat 2 strings based on index
first_name = "Julie"
last_name = "Blevins"
def account_generator(first_name, last_name):
  return first_name[:3] + last_name[:3]
new_account = account_generator(first_name, last_name)

# similar example as to the one above using concat of 2 strings
first_name = "Reiko"
last_name = "Matsuki"
def password_generator(first_name, last_name):
  return first_name[-3:] + last_name[-3:]
temp_password = password_generator(first_name, last_name)
print(temp_password)

# example of concat 2 strings
first_name = "Reiko"
last_name = "Matsuki"
def password_generator(first_name, last_name):
  return first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
temp_password = password_generator(first_name, last_name)
print(temp_password)

# examples of using the len method on strings
# length of strings
favorite_fruit = "blueberry"
length = len(favorite_fruit)
print(length)
# Output: 9

last_char = favorite_fruit[len(favorite_fruit)-1]
print(last_char)
# Output: y

length = len(favorite_fruit)
last_chars = favorite_fruit[length-4:]
print(last_chars)

# example of correcting a string value
# cant change a string only change it by assigning it to a new variable
first_name = "Bob"
last_name = "Daily"
fixed_first_name = "R" + first_name[1:]
print(first_name,last_name)
print(fixed_first_name,last_name)

#example of function and loop that iterates through the string
def print_each_letter(word):
  for letter in word:
    print(letter)

favorite_color = "blue"
print_each_letter(favorite_color)
# => 'b'
# => 'l'
# => 'u'
# => 'e'

# example of function and loop to iterate through string
def get_length(word):
  counter = 0
  for letter in word:
    counter += 1
  return counter

# strings and conditionals statements
favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)

# example of function to check string
def  letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

# strings and conditionals using the in statement
print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False
print("e" in "blueberry" and "e" in "carrot")
# => False
print("e" in "blueberry" and not "e" in "carrot")
# => True

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

# examples of using classes and _init_ and _repr_ method on strings
# how strings are displayed using the __repr__() dunder method - only self parameter
class Employee():
  def __init__(self, name):
    self.name = name
argus = Employee("Argus Filch")
print(argus)
# prints "<__main__.Employee object at 0x104e88390>"

# example function on strings
class Employee():
  def __init__(self, name):
    self.name = name
   def __repr__(self):
    return self.name
 argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"

# example function on strings
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    self.radius = diameter / 2
  def area(self):
    return self.pi * self.radius ** 2
  def circumference(self):
    return self.pi * 2 * self.radius
  def __repr__(self):
    return 'Circle with radius {radius}'.format(radius=self.radius) 
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
print(medium_pizza)
print(teaching_table)
print(round_room)


# String Methods - various methods that you can use on strings
#A single character can be accessed with bracket notation ( [index] ), or a substring can be accessed using slicing
#( [start:end] ).
#Indexing with negative numbers counts from the end of the string.
# example of indexing and slicing strings - 
str = 'yellow'
str[1] # => 'e'
str[-1] # => 'w'
str[4:6] # => 'ow'
str[:4] # => 'yell'
str[-3:] # => 'low'

#example of using title() method - returns string in title case
my_var = "dark knight"
print(my_var.title())
# Prints: Dark Knight

# formatting strings with 
# .lower() and .upper() and .title()
favorite_song = 'SmOoTH'
favorite_song_lowercase = favorite_song.lower()
print(favorite_song_lowercase)
# => 'smooth'
print(favorite_song)
# => 'SmOoTH'
poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)
poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)

#exaple lower() method
greeting = "Welcome To Chili's"
print(greeting.lower())
# Prints: welcome to chili's

#example of upper method
dinosaur = "T-Rex"

print(dinosaur.upper())
# Prints: T-REX

# .split() seperates each element of the string
man_its_a_hot_one = "Like seven inches from the midday sun"
print(man_its_a_hot_one.split())
# => ['Like', 'seven', 'inches', 'from', 'the', 'midday', 'sun']
line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one)
print(line_one_words)

# can also use split() to select a specific destination.  
greatest_guitarist = "santana"
print(greatest_guitarist.split('n'))
# => ['sa', 'ta', 'a']
print(greatest_guitarist.split('a'))
# => ['s', 'nt', 'n', '']

# example using split and append
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(',')
print(author_names)
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
print(author_last_names)

# example of split using \n and \t to split to multi line or horizontal tab
smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""
chorus_lines = smooth_chorus.split('\n')
print(chorus_lines)

# example of split using \n and \t
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""
spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

# example of using split, strip and append
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
print(highlighted_poems_stripped)
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(":"))
titles = [] 
poets = []
dates = []
for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])
for i in range(0,len(highlighted_poems_details)):
  print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))

# example of strip() method
text1 = ' apples and oranges '
text1.strip() # => 'apples and oranges'
text2 = '...+...lemons and limes...-...'

# Here we strip just the "." characters
text2.strip('.') # => '+...lemons and
limes...-'

# Here we strip both "." and "+"
characters
text2.strip('.+') # => 'lemons and
limes...-'

# Here we strip ".", "+", and "-"
characters
text2.strip('.+-') # => 'lemons and limes'

# .strip() - removes all the whitespaces from a string
featuring = "           rob thomas                 "
print(featuring.strip())
# => 'rob thomas'

# strip using a special character
featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!'))
# => 'rob thomas       '

# example of strip
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
love_maybe_full = '\n'.join(love_maybe_lines_stripped) 
print(love_maybe_full)

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

# example of format() method
msg1 = 'Fred scored {} out of {} points.'
msg1.format(3, 10)
# => 'Fred scored 3 out of 10 points.'
msg2 = 'Fred {verb} a {adjective} {noun}.'
msg2.format(adjective='fluffy',
verb='tickled', noun='hamster')
# => 'Fred tickled a fluffy hamster.'

# example of join method joining strings together
# using the .join() method to put strings together must run on a ' '  space
my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'
print(''.join(my_munequita))
# => 'MySpanishHarlemMonaLisa'
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

#example of join method
x = "-".join(["Codecademy", "is","awesome"])
print(x)
# Prints: Codecademy-is-awesome

#  using a space to create a sentance from various strings
santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']
santana_songs_csv = ','.join(santana_songs)
print(santana_songs_csv)
# => 'Oye Como Va,Smooth,Black Magic Woman,Samba Pa Ti,Maria Maria'

# escape sequences - taking a list of strings and using the \n delimeter to put them on seperate lines
smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio', 'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']
smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)
print(smooth_fifth_verse)

# puts each one on a seperate line
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

# example of find method - searches a string and retuns the first index of value
print('smooth'.find('t'))
# => '4'
print("smooth".find('oo'))
# => '2'
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)

# example of replace method - replaces one argument with another one
#  string_name.replace(substring_being_replaced, new_substring)
with_spaces = "You got the kind of loving that can be so smooth"
with_underscores = with_spaces.replace(' ', '_')
print(with_underscores)
# 'You_got_the_kind_of_loving_that_can_be_so_smooth'

# example of replace - the \ and having """ will let the string start on the next line
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace('Tomer', "Toomer")
print(toomer_bio_fixed)





















































