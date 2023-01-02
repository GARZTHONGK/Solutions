"""
Exercise "Animals"

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

All you need to know in order to solve this exercise, you'll find in the cars_oop- and rpg1-files.

Define a class named Animal.
Each object of this class shall have the attributes name, sound, height, weight, legs, female.
Name and sound are strings. Height and weight are floating point numbers. Legs is a integer. Female is boolean.

Add to the class meaningful methods __init__ and __repr__.
Call these methods to create objects of the class Animal and to print them out in the main program.

Write a class method named make_noise, which prints out the animal's sound in the console.
Call this method in the main program.

Define another class Dog, which inherits from Animal.
Each object of this class shall have the attributes tail_length and hunts_sheep.
Tail_length is a floating point number. Hunts_sheep is boolean.

Add to the class meaningful methods __init__ and __repr__.
In writing the constructor of Dog, try to reuse code from the class Animal.
Call these methods to create objects of the class Dog and to print them out in the main program.

Call the method make_noise on Dog objects in the main program.

Write a class method named wag_tail for Dog.
This method prints out into the console something like
"The dog Snoopy wags its 32cm long tail"
Call this method in the main program.

Write a function mate(mother, father). Both parameters are of type Dog.
This function shall return a new object of type Dog.
In this function, make meaningful rules for the new dogs attributes.
Make sure that this function only accepts dogs with the correct sex as arguments.

In the main program, call this method and print out the new dog.

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""
import random
from random import randrange
from random import randint
class Animal():
    def __init__(self, name, sound, height, weight, legs, female):
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female


    def __repr__(self):
        return f"Animals stats: name: {self.name}, sound: {self.sound}, height: {self.height}, weight:{self.weight}, legs: {self.legs} gender=female: {self.female}"

    def make_noise(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self, name, sound, height, weight, legs, female, tail_length, hunts_sheep):
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female
        self.tail_length = tail_length
        self.hunts_sheep = hunts_sheep

    def __repr__(self):
        return f"Dogs stats: name: {self.name}, sound: {self.sound}, height: {self.height}, weight:{self.weight}, legs: {self.legs} gender=female: {self.female} tail_length: {self.tail_length}, hunts_sheep: {self.hunts_sheep}"

    def wag_tail(self):
        print(f"The dog {self.name} wags it's {self.tail_length}cm long tail")

def mate(mate1, mate2):
    if type(mate1) == type(mate2):
        print(f"{mate1.name} and {mate2.name} are the same animal")
        if not mate1.female and mate2.female or mate1.female and not mate2.female:
            if type(mate1) == Dog:
                print(f"Breeding {mate1.name} and {mate2.name}")

                name = dghggs
                sound = "woof"
                if mate1.height > mate2.height:
                    height = randint(mate2.height, mate1.height)
                else:
                    height = randint(mate1.height, mate2.height)

                if mate1.weight > mate2.weight:
                    weight = randint(mate2.weight, mate1.weight)
                else:
                    weight = randint(mate1.weight, mate2.weight)
                legs = 4

                female = bool(randint(1,10) % 2)
                if mate1.tail_length > mate2.tail_length:
                    tail_length = randint(mate2.tail_length, mate1.tail_length)
                else:
                    tail_length = randint(mate1.tail_length, mate2.tail_length)
                tail_length = randint(mate1.tail_length, mate2.tail_length)
                hunts_sheep = True
                puppy1 = Dog(name, sound, height, weight, legs, female, tail_length, hunts_sheep)
                print(puppy1)
            else: print("invalid animal")
    else:
        print(mate1.name, " and ", mate2.name, " cannot breed!")

animal1 = Animal("Torben", "MEEAOOAOOWW", 40, 10, 4, True)
print(animal1)
animal1.make_noise()
print("\n")

dog1 = Dog("Robert", "WOOF", 60, 30, 4, False, 20, True)
dog2 = Dog("Marie", "wof", 55, 30, 4, True, 20, True)
print(dog1)
dog1.make_noise()
dog1.wag_tail()
print(type(dog1))
# print(dog2)
print("\n")
mate(dog1, dog2)
# print(randrange(10,20))
# print(type(dog2))
print(Puppy1)


