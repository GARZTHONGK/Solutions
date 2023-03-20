"""
Exercise "Cars":

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

define a function that prints a car's motor sound (for example "roooaar")

in the main program:
define variables which represent the number of wheels and the maximum speed of 2 different cars
print out these properties of both cars
then call the motor sound function

if you have no idea how to begin, open S0046_cars.py and start from there
if you get stuck, ask google, the other pupils or the teacher (in this order).
if you are still stuck, open S0047_cars.py and compare it with your solution

Compare your program to the teacher's solution in S0047_cars.py

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""
def engine_start():
    print("WROOM")

car1_wheels = 4
car1_maxspeed = 200
car2_wheels = 4
car2_maxspeed = 160

print("Car 1: \n","Wheels:", car1_wheels,"\n", "Max Speed:", car1_maxspeed)
engine_start()

print("Car 2: \n","Wheels:", car2_wheels,"\n", "Max Speed:", car2_maxspeed)
engine_start()