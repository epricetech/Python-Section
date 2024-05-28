# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:43:57 2023

@author: geron
"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters += [letter.lower() for letter in letters] # puts in lowercase values as well and the 2nd line creates the points list for those lowercase
points *= 2
letter_to_points = {key:value for key, value in zip(letters, points)}  # zips to lists together into a dictionary
letter_to_points[' '] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total
#print(point_total)

brownie_points = score_word('BROWNIE')
print(brownie_points)

player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 
                   'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 
                   'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 
                   'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}


# to turn nested loop into function to call anytinme a word is played
player_to_points = {}
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
        
update_point_totals()
print(player_to_points)


# function that take a player and word and add word to list they have played

def play_word(player, word):
    player_to_words[player].append(word)
    update_point_totals()
play_word('player1', 'CODE')
print(player_to_words)
print(player_to_points)







