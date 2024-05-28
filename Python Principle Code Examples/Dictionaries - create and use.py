# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 11:31:26 2023

@author: geron
"""

# dictionaries - another way to do lists but its an unorded set of keys and value pairs seperated by key:valuepair
# you can map pieces of these pares to each other to find associated values
#  dictionaries can include strings or numbers or lists or other dictionaries or booleans - and you can mix match
# value types - lists cant be the key portion - and key must always be an immutable data type such as string, number or tuples
# example you can see keys are strings or numbers(int or float) the values are many vaired data type
dictionary = {1: 'hello','two': True,'3': [1, 2, 3],'Four': {'fun': 'addition'},5.0: 5.5}
# they can be many types like strings or numbers or lists or other dicitonaries
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}
# you can mix match values types as well - lists cant be the key portion.  only value portion
person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}
# to define a list you must use {}
#  Syntax example
roaster = {"q1": "Ashley", "q2": "Dolly"}

# you can also create an empty dictionary with {}
empty_dict = {}

# you can use the update method or call the specific key to change the value
dict1 = {'color': 'blue', 'shape':'circle'}
dict2 = {'color': 'red', 'number': 42}
dict1.update(dict2)
# dict1 is now {'color': 'red', 'shape':'circle', 'number': 42}

# or you can call the specific key or value to change
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["cheesecake"] = 8
print(menu)

# example of updating an empty dictionary with key and value pairs
#can be used to add or overwrite keys and values
animals_in_zoo = {}
animals_in_zoo['zebras'] = 8
animals_in_zoo['monkeys'] = 12
animals_in_zoo['dinosaurs'] = 0
print(animals_in_zoo)

# example of updating dictionary with key and value
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners['Supporting Actress'] = 'Viola Davis'
oscar_winners['Best Picture'] = 'Moonlight'
print(oscar_winners)

# examples of using the update method
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print(sensors)

# examples of using the update method
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({'theLooper': 138475, 'stringQueen': 85739})
print(user_ids)

# example of taking 2 lists and making a dictionary
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

#example of taking 2 lists and making a dictionary and updaing the dictionary
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
plays['Purple Haze'] = 1
plays['Respect'] = 94
library = {'The Best Songs': plays, 'Sunday Feelings': {}}
print(library)

#accessing and writing data example
my_dictionary = {"song": "Estranged",
"artist": "Guns N' Roses"}
print(my_dictionary["song"])
my_dictionary["song"] = "Paradise City"

# example of how to acces dictionary using key
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
building_heights["Burj Khalifa"]
building_heights["Ping An"]

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements['earth'])
print(zodiac_elements['fire'])


# check to see if there is a value in a dictionary
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
key_to_check = "Landmark 81"
 # checks to see if in dictionary and returns a false if not there
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
zodiac_elements['energy'] = "Not a Zodiac element"
if 'energy' in zodiac_elements:
  print(zodiac_elements["energy"])


# Dictionary Key-Value methods - when you need to look at the info in the dictionry these methods return objects
# that contain the dicitonary key and values
# methods
# 1. .keys() - returns the key through a dict_keys object
# 2.  .values() - returns the values through a dict_values object
# 3.  .items() - returns both the keys and values through a dict/_items object
ex_dict = {"a": "anteater", "b":"bumblebee", "c": "cheetah"}

ex_dict.keys()
# dict_keys(["a","b","c"])
ex_dict.values()
# dict_values(["anteater", "bumblebee","cheetah"])

ex_dict.items()
# dict_items([("a","anteater"),("b","bumblebee"),("c","cheetah")])

# keys method example
# this one really doesnt run
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
list(test_scores)["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
for student in test_scores.keys():
  print(student)

# example of keys method
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)

# values method example
#  can use .values() to get the values for the keys in the dictionary
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
for score_list in test_scores.values():
  print(score_list)
 #  to put al the values in a list 
list(test_scores.values()) 
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for exercises in num_exercises.values():
  total_exercises += exercises
  print(total_exercises)

# items method example
#  .items() - will get both key and value from dictionary
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for position, num in pct_women_in_occupation.items():
  print('Women make up ' + str(num) + ' percent of ' + position + 's')

# .get() method to acces a dictionary value if it exists.  Method takes key as first argument and an optional defualt
# value as the second argument.  If no specific 2nd argument and key is not found it will return none
# without default
{"name": "Victor"}.get("name")
# returns "Victor"

{"name": "Victor"}.get("nickname")
# returns None

# with default
{"name": "Victor"}.get("nickname","nickname is not a key")
# returns "nickname is not a key"

# can use the .get() to get a key instead of using variable{key} - will also not return an keyerror if the
# key doesnt exist
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
#this line will return 632:
building_heights.get("Shanghai Tower")
#this line will return None:
building_heights.get("My House")
print(building_heights.get('Shanghai Tower', 0))
print(building_heights.get('Mt Olympus', 0))
print(building_heights.get('Kilimanjaro', 'No Value'))

#example using the get method
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get('teraCoder', 10000)
print(tc_id)
stack_id = user_ids.get('superStackSmash', 100000)
print(stack_id)

# .pop() method can remove k-value pairs - it takes the key as an argument and at the same time also returns the value
# that it removes from the dictionary
famous_museums = {'Washington':
'Smithsonian Institution', 'Paris': 'LeLouvre', 'Athens': 'The Acropolis Museum'}
famous_museums.pop('Athens')
print(famous_museums) 
# {'Washington':'Smithsonian Institution', 'Paris': 'LeLouvre'}

# to delete a key use the .pop() command
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(320291, "No Prize"))
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(100000, "No Prize"))
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(872921, "No Prize"))
raffle = {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}

# example using pop to remove key value
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop('stamina grains',0)
health_points += available_items.pop('power stew', 0)
health_points += available_items.pop('mystic bread', 0)
print(available_items)
print(health_points)


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


#Write your word_length_dictionary function here:  word length dictionary
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



















