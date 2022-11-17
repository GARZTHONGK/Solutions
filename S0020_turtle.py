"""
Exercise "Tom the Turtle":

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

The function "demo" introduces you to all commands you need to interact with Tom in the following exercises.

Only if you are curious and love details:
    Here is the full turtle graphics documentation:
    https://docs.python.org/3.3/library/turtle.html

Part 1:
    Write a function "square" which accepts a parameter "length".
    Calling this function causes the turtle to draw a square with a side length of "length" pixels.

Part 2:
     Write a function "visible" which returns a boolean value,
     indicating if the turtle is in the visible area of the screen.
     Use this function in the following parts of this exercise
     to return the turtle to the screen when it wandered off.

Part 3:
    Write a function "many_squares" with a for loop, which calls square repeatedly.
    Use this function to draw several squares of different sizes in different positions.
    The function shall have some parameters. For example:
        number: how many squares will be drawn?
        size: how large are the squares?
        distance: how far away from the last square is the next square positioned?

Part 4:
    Write a function that produces patterns similar to this:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Part 5:
    Write a function that produces patterns similar to this:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    The function shall have a parameter, that influences the shape of the pattern.

Part 6:
    Create your own function that produces a cool pattern.
    Later, if you like, present your pattern on the big screen to the others.

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""


import turtle    # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.


def demo():  # demonstration of basic turtle commands

    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):
        tom.forward(100)  # move 100 pixels
        tom.left(45)  # turn 45 degrees left
        print("Tom is now at", tom.position())
    tom.penup()  # do not draw while moving
    tom.forward(222)
    tom.pendown()  # draw while moving
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(333)
    tom.home()  # return to the original position in the middle of the window
    turtle.done()  # keeps the turtle window open after the program is done

def square(Length):


    tom.forward(Length)
    tom.right(90)
    tom.forward(Length)
    tom.right(90)
    tom.forward(Length)
    tom.right(90)
    tom.forward(Length)
    tom.right(90)



def visible():
    tom = turtle.Turtle()
    print(type(tom))
    tom.isvisible() #checks if turtle is visible


def many_squares(number,size,distance):


    for x in range(number):
        print("starting round", x)
        print("calling square...")
        square(size)
        print("Square drawn")
        print("Lifting pen...")
        tom.penup()
        print("Moving ", distance," to right")
        tom.forward(distance)
        print("Stopped moving")
        print("Toms current position is: ",tom.position)
        print("Putting down pen...")
        tom.pendown()

def spiral_square(StartLength):
    percentage = 0.05 * StartLength #finds percentage of input
    print(percentage, " Is how much to minus each turn")
    i = 1
    while i > 0:
        tom.forward(StartLength)
        tom.right(90)
        StartLength = StartLength - percentage
        print(StartLength)
        if StartLength <= 0:
         break


def star_pattern(turnPower):
    i = 1
    while i > 0:
        tom.right(turnPower)
        tom.forward(100)
        print("executed")


def cool_pattern(triangleTurn, circleTurn, length, amount):
    i = 1
    percentageOfLength = 0.1 * length
    for x in range(amount): # makes 2/3 of a triangle
        tom.right(triangleTurn)
        tom.forward(length)
        tom.right(triangleTurn)
        tom.forward(length)
        for x in range(20): # makes half of a circle

            tom.forward(percentageOfLength)
            tom.right(circleTurn)





tom = turtle.Turtle()  # create an object named tom of type Turtle
print(type(tom))

#demo()
#square(400)
#many_squares(10,50,100)
#spiral_square(100)
#star_pattern(160)
cool_pattern(130, 10, 100, 7)





turtle.done()