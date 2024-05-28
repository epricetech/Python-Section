# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 11:36:20 2023

@author: geron
"""

#  this code is not the best and not sure if it works.  structure seems a bit off in a few parts
# Let’s start by taking a look at what the mazes files look like!

# This one is maze_data_1.csv:

# #,#,#,#,#,#,#,#,#,#
# #,_,_,_,#,_,_,_,$,#
# #,_,A,_,_,_,#,_,_,#
# #,B,_,_,#,_,#,_,_,#
# #,_,C,_,#,_,_,_,_,#
# #,#,#,#,#,#,#,#,#,#
# The mazes are csv files which contain different characters that represent different objects in the robot race. 
# Any letter represents a robot, the # character represents a wall which the robots can collide with, and the $ is 
# the goal which the robots are racing towards. Robots can traverse into any empty space (shown by an _) and 
# they can even occupy the same space as another robot (shown as a +). At any point during this project, 
# feel free to create your own csv maze and use it in the code instead of the example ones.


# Stuck? Get a hint
# 2.
# Now take a look at the robot_race.py file. After importing the required modules and classes, there are some 
# values to take note of at the top of the file. The maze_file_name can be changed to any csv file which follows
#  the maze structure (as defined earlier). The seconds_between_turns value will determine how much time passes 
#  between updating the visualized maze in the console (which we will be coding during the project). Finally, 
#  the max_turns value determines how many turns the robots have before the race ends. The race will end if the
#  max turns are reached or if all of the robots reach the goal.

# The robots will be scored based on the amount of moves they make plus the number of collisions they have with the walls. The robot with the lowest score wins.


# Stuck? Get a hint
# 3.
# Throughout this project, run the code in the terminal by using the command: python3 robot_race.py

# Commanding the Bots
# 4.
# To begin, we are going to use the provided compute_robot_logic function from robot_race_functions.py 
# to calculate every move for every robot which has not finished the maze yet. This function accepts the walls, 
# goal, and bot variables in that order and returns a tuple containing the robot name, selected action, and if 
# the robot has collided.

# 5.
# The first while loop iterates until the race is over. Inside of this, loop through every bot which has not 
# finished the race yet (bot.has_finished == False). Pass the walls, goal, and bot to the compute_robot_logic 
# function in that order. This will return the robot’s decision given its position in the map in the form of a 
# tuple containing (robot_name, action, has_collided). Append the robot’s decision to the robot_moves deque.


# Hint
# Within the for loop which iterates through every robot which has not finished the maze yet, appending the 
# computed command to the deque could look like:

# robot_moves.append(rr.compute_robot_logic(walls, goal, bot))
# Scoring the Bots
# 6.
# Now that all robots’ moves have been calculated, we can use that data and the Counter container to find the 
# exact number of moves that each robot makes using one line of code! This should count every name 
# (the first element in the move tuple) for every move in the deque.


# Hint
# In order to automatically count the number of moves based on the robot names, we can count based on number 
# of occurances of each robot name in the robot_moves deque.

# The Counter constructor could look like:

# Counter(move[0] for move in robot_moves)
# 7.
# We can use the Counter container to count how many collisions each robot made as well. To do this, make 
# sure to only count the robot name when has_collided is True in each move tuple within the robot_moves deque.


# Hint
# To count while checking if a collision occurred, we need to test if the third element of the move tuple is True. 
# This is similar to the last step, but it includes a conditional statement as well:

# The constructor could look like:

# Counter(move[0] for move in robot_moves if move[2] == True)
# 8.
# Since we have the move and collision count for each robot, we can now calculate the final scores for each bot. 
# In order to make it easier to read, let’s create a namedtuple to keep track of our bot score data. 
# Create a namedtuple subclass called BotScoreData which contains the 
# field names: 'name', 'num_moves', 'num_collisions', and 'score'.


# Hint
# Remember, in order to create a namedtuple subclass, we use the 
# constructor: namedtuple('typename', ['field_name_1', 'field_name_2', etc.])

# 9.
# Loop through each of the robots in bots, and for every robot, create a new BotScoreData object containing 
# all the correct data. Append this new object to the bot_scores list. Remember that the score for each robot 
# is found by adding the number of moves and the number of collisions. Try calling the print_results function 
# using the bot_scores and see what’s printed to the console. You should see the final results of the race in 
# the terminal, but now let’s watch them actively move through the maze!


# Hint
# Remember to calculate the score for each robot by adding each bot’s collisions and number of movements. 
# Create a new object of the robot scoring namedtuple subclass which was created and append it to the bot_scores list.

# This could look like:

# bot_scores.append(BotScoreData(bot.name, move_count, collision_count, move_count + collision_count))
# Displaying the Live Race
# 10.
# To watch the robots travel through the maze, let’s start by creating a dict which allow us to easily access 
# each robot object by its name when looking at the different moves in the deque. Loop through every robot in 
# bots and add it to bot_data using the robot name as the key and the robot object as the value.


# Hint
# Use a for loop to iterate through each bot in bots. Inside of this loop, the robot can be added to the 
# dictionary by name using:

# bot_data[bot.name] = bot
# 11.
# Create a loop which continues while moves still exist in the robot_moves deque. For every iteration, 
# pop the move from the front of the deque and call the process_move method on the bot accessed from the bot_data. 
# The process_move accepts a string which represents an action. This is found in the second element of each move 
# tuple from the robot_moves deque (move[1]).

# The next three lines of code update the character maze with the new robot positions, prints the maze, 
# and pauses the program briefly based on the settings from the top of the script.


# Hint
# Use a while loop which continues as long as the length of robot_moves is greater than 0. In this loop, 
# pop the next move from the front of the moves deque and use the bot name (move[0]) to access the bot 
# and .process() the action (move[1]).

# This could look like:

# bot_name, direction, has_collided = robot_moves.popleft()
# bot_data[bot_name].process_move(direction)
# 12.
# Finally, remove the call to rr.print_results(bot_scores) from earlier in the code and place it at the 
# end of the code to see the final results after the race!

# 13.
# In the terminal, type python3 robot_race.py in order to watch the robots race and see the final results. 
# Try the other mazes, make some new ones, and change the settings at the top of robot_race.py Great job completing 
# the project!


import csv
import random as rand


def read_maze(name):
    maze_chars = []
    with open(name, 'r') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            maze_chars.append(row)
    return maze_chars


def print_maze(maze_data):
    for row in maze_data:
        printed_row = ''
        for col in row:
            printed_row += col + '  '
        print(printed_row)
    print('\n')

def is_race_over(bots):
    done = True
    for bot in bots:
        if not bot.has_finished:
            done = False
    return done


def print_results(bot_score_data):
    bot_score_data.sort(key=lambda b: b.score)
    place = 1
    print("----- RESULTS -----")
    for score_data in bot_score_data:
        print(str(place) + '. Robot: ' + str(score_data.name))
        print('  ' +  'Score: ' + str(score_data.score) + ' Moves: ' + str(score_data.num_moves) + ' Collisions: ' + str(score_data.num_collisions))
        place += 1


def process_maze_init(maze_data):
    walls = []
    goal = None
    bots = []
    for r, row in enumerate(maze_data):
        for c, col in enumerate(row):
            if col == '#':
                walls.append(Wall(c,r))
            elif col == '$':
                goal = Goal(c,r)
            elif col.isalpha():
                bots.append(Robot(c,r, col))
    return [walls, goal, bots]


def compute_robot_logic(walls, goal, bot):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    move_names = {(-1, 0): 'left', (1, 0): 'right', (0, -1): 'down', (0, 1): 'up', (0, 0): 'nothing'}

    selected_move = moves[rand.randint(0,3)]
    move_dist = []
    for m, move in enumerate(moves):
        dist = calc_manhattan_dist(bot.calc_x + move[0], bot.calc_y + move[1], goal.x, goal.y)
        move_dist.append([m,dist])
    move_dist.sort(key=lambda x: x[1])
    if rand.random() < 0.45:
        selected_move = moves[move_dist[0][0]]

    hit_wall = False
    for wall in walls:
        if bot.calc_x + selected_move[0] == wall.x and bot.calc_y + selected_move[1] == wall.y:
            hit_wall = True

    found_alternate_move = False
    if hit_wall:
        for next_move in move_dist:
            move = moves[next_move[0]]
            hit_wall_move = False
            for wall in walls:
                if bot.calc_x + move[0] == wall.x and bot.calc_y + move[1] == wall.y:
                    hit_wall_move = True

            if not hit_wall_move:
                selected_move = move
                found_alternate_move = True
                break

        if not found_alternate_move:
            selected_move = (0,0)

    if bot.calc_x + selected_move[0] == goal.x and bot.calc_y + selected_move[1] == goal.y:
        bot.has_finished = True
        bot.calc_x += selected_move[0]
        bot.calc_y += selected_move[1]
        return bot.name, 'finished', hit_wall

    bot.calc_x += selected_move[0]
    bot.calc_y += selected_move[1]
    return bot.name, move_names[selected_move], hit_wall


def update_maze_characters(old_maze_chars, bots):
    to_replace = []
    for r, row in enumerate(old_maze_chars):
        for c, col in enumerate(row):
            if col.isalpha() or col == '+':
                to_replace.append((c,r))
    for elem in to_replace:
        old_maze_chars[elem[1]][elem[0]] = '_'
    for bot in bots:
        if not bot.remove:
            if old_maze_chars[bot.y][bot.x].isalpha():
                old_maze_chars[bot.y][bot.x] = '+'
            else:
                old_maze_chars[bot.y][bot.x] = bot.name


def calc_manhattan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


class Robot:
    def __init__(self, x, y, name):
        self.x = x
        self.calc_x = x
        self.y = y
        self.calc_y = y
        self.has_finished = False
        self.remove = False
        self.name = name

    def process_move(self, direction):
        if direction == 'left':
            self.x += -1
        if direction == 'right':
            self.x += 1
        if direction == 'up':
            self.y += 1
        if direction == 'down':
            self.y += -1
        if direction == 'finished':
            self.remove = True


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Goal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
import robot_race_functions as rr
from collections import deque, Counter, namedtuple
from time import time, sleep

maze_file_name = 'maze_data_1.csv'
seconds_between_turns = 0.3
max_turns = 35

# Initialize the robot race
maze_data = rr.read_maze(maze_file_name)
rr.print_maze(maze_data)
walls, goal, bots = rr.process_maze_init(maze_data)

# Populate a deque of all robot commands for the provided maze
robot_moves = deque()
num_of_turns = 0
while not rr.is_race_over(bots) and num_of_turns < max_turns:
  # For every bot in the list of bots, if the bot has not reached the end, add a new move to the robot_moves deque
  # Add your code below!
  for bot in bots:
    if bot.has_finished == False:
      robot_moves.append(rr.compute_robot_logic(walls, goal, bot))
  num_of_turns += 1

# Count the number of moves based on the robot names
# Add your code below!
num_moves = Counter(move[0] for move in robot_moves)


# Count the number of collisions by robot name
# Add your code below!
num_collisions = Counter(move[0] for move in robot_moves if move[2] == True)

# Create a namedtuple to keep track of our robots' points
# Add your code below!
BotScoreData = namedtuple('BotScoreData', ['name', 'num_moves', 'num_collisions', 'score'])

# Populate a dict to keep track of the robot movements
# Add your code below!
bot_scores = []
for bot in bots:
  score = num_moves[bot] + num_collisions[bot]
  bot_scores.append(BotScoreData(bot.name, num_moves[bot], num_collisions[bot], score))


bot_data = {}
for bot in bots:
  bot_data[bot.name] = bot

# Move the robots and update the map based on the moves deque
while len(robot_moves) > 0:
  # Make sure to pop moves from the front of the deque
  # Add your code below!
  bot_name, move, hit_wall = robot_moves.popleft()
  bot_data[bot_name].process_move(move)

  # Update the maze characters based on the robot positions and print it to the console
  rr.update_maze_characters(maze_data, bots)
  rr.print_maze(maze_data)
  sleep(seconds_between_turns - time() % seconds_between_turns)

# Print out the results!
rr.print_results(bot_scores)       
        




















