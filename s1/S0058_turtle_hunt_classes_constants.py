"""
Exercise "Turtle Hunt":

As always, read the whole exercise description carefully before you begin to solve the exercise.

The game:
    This exercise is a game for 2 players.
    3 Turtles (hunters) are trying to catch another turtle (prey) as fast as possible.
    One player controls the prey, the other player controls the hunters. Then the players switch roles.
    In each turn the players decide how many degrees their turtle(s) rotate(s). This is the player's only task.
    The prey gets one point for every turn before it gets caught.
    If the prey is still on the run after MAX_TURNS turns, the points double and the hunt ends.


The code for the game is already written in S0058_turtle_hunt_main.py. Do not change that file.

Your job is to make the turtles rotate smarter.

Copy this file and S0058_turtle_hunt_main.py into your own solution directory.
Write your solution into your copy of S0058_turtle_hunt_classes_constants.py.

File structure:
    The code is divided into 2 files in order to make it clear which part of the code
    you are supposed to change and which part of the code you shall leave unchanged.

    S0058_turtle_hunt_main.py:
        This is the main program.
        Do not make changes therein.
        Run it in order to start the game.

    This file (S0058_turtle_hunt_classes_constants.py):
        All your programming for this exercise happens in this file.

Step 1:
    Understand the program code as it is now.
    You do not need to understand every detail of the main program though.
    Understand when and how the methods rotate_prey() and rotate_hunt() are used.
    From now on, all your programming for this exercise happens in this file here.

Step 2:
    Change the name of class PlayerName1 in the first line of it's class definition to your personal class name.
    At the bottom of this file, set the variables class1 and class2 to your personal class name.

Step 3:
    In your personal class, make the methods rotate_prey and rotate_hunter smarter.
    Possibly you'll also want to add some attributes and/or methods to your class.
    You may not manipulate (e.g. move) the turtles with your code though.

Step 4:
    Find a sparring partner in your study group.
    As with everything else, ask your teacher for help, if needed.
    In your code, replace the whole class PlayerName2 with your sparring partner's class.
    At the bottom of this file, set the variable class2 to your sparring partner's class name.
    Let the 2 classes fight and learn from the results in order to improve your code.
    Repeat this step until you are happy :-)

Step 5:
    When your program is complete, push it to your github repository.
    Then send this Teams message to your teacher: <filename> done
    Thereafter go on with the next file.

Later:
    When everyone is done with this exercise, we will hold a tournament
    to find out, who programmed the smartest turtles :)

Only if you are curious and love details:
    Here is the full turtle graphics documentation:
    https://docs.python.org/3.3/library/turtle.html
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
import random
import math


class Albert(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.count = 10
        self.degree = 0


    def rotate_prey(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        # self: the turtle that shall be rotated
        # positions: a list of tuples. Each tuple is a pair of coordinates (x,y).
        # positions[0] is the coordinate tuple of the prey. positions[0][0] is the x-coordinate of the prey.
        # positions[1], positions[2], positions[3] refer to the hunters.
        # for example is positions[3][1] the y-coordinate of the third hunter.
        # degree = 0
        degree = self.degree

        print(distance(positions[0],positions[1]), distance(positions[0],positions[2]),distance(positions[0],positions[3]))
        print(findclosest(positions))
        if self.count % 10 == 0:
            degree = 0
            degree += direction(positions[0], findclosest(positions)) - 180



        self.count += 1
        print("current degree =",degree, direction(positions[0], positions[1]))

        self.degree = degree
        return degree

    def rotate_hunter(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        degree = 0
        return degree

def distance(pos1, pos2):  # calculate the distance between 2 points with the Pythagorean equation
    delta_x = pos1[0] - pos2[0]
    delta_y = pos1[1] - pos2[1]
    return math.sqrt(delta_x ** 2 + delta_y ** 2)

def findclosest(positions):
    closestpos = positions[1]
    if distance(positions[0],positions[2]) < distance(positions[0], positions[1]):
        closestpos = positions[2]
    if distance(positions[0],positions[3]) < distance(positions[0], positions[1]) or distance(positions[0], positions[3]) < distance(positions[0], positions[2]):
        closestpos = positions[3]
    return closestpos

def direction(start_position, end_position):
    # returns the direction from start_position to end_position in degrees
    # 0° is east (plus x-axis), which is also the direction of each turtle at the beginning of each hunt.
    # 90° is south (minus y-axis), 180° is west (minus x-axis), 270° is north (plus y-axis)
    delta_x = end_position[0] - start_position[0]
    delta_y = end_position[1] - start_position[1]
    angle = math.atan2(delta_y, delta_x) * 180 / math.pi
    if delta_y < 0:
        return -angle
    else:
        return 360 - angle

#  Insert the code of your sparring partner's turtle class here:
#
#
#
#


# change these global constants only for debugging purposes:
MAX_TURNS = 100       # Maximum number of turns in a hunt.                           In competition: probably 200.
ROUNDS = 1            # Each player plays the prey this often.                       In competition: probably 10.
STEP_SIZE = 3         # Distance each turtle moves in one turn.                      In competition: probably 3.
SPEED = 0             # Fastest: 10, slowest: 1, max speed: 0.                       In competition: probably 0.
CAUGHT_DISTANCE = 10  # Hunt is over, when a hunter is nearer to the prey than that. In competition: probably 10.


random.seed(2)  # use seed() if you want reproducible random numbers for debugging purposes. You may change the argument of seed().


class1 = Albert  # (red prey) Replace PlayerName1 by your own class name here.
class2 = Albert  # (green prey) For testing your code, replace PlayerName1 by your own class name here. Later replace this by your sparring partner's class name.
