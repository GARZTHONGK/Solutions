"""
Exercise: Object oriented role playing game, part 1 :

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Define a class "Character" with attributes "name, max_health", "_current_health", "attackpower."
_current_health shall be a private attribute, it is not meant to be changed from outside the class.

Add a constructor (__init__) which accepts the classes' attributes as parameters.
Add a method for printing out class objects (__repr__).

Add a method "hit" which reduces _current_health of another character by attackpower.
Example: _current_health=80 and attackpower=10: a hit reduces _current_health to 70.

The method hit may not change the private attribute _current_health of a (potentially) foreign class.
For this reason we define another method get_hit which reduces _current_health of the object it belongs to by attackpower.

If you get stuck, ask google, the other pupils or the teacher (in this order).
If you have no idea how to begin, open S0061_rpg1_help.py and start from there.

When your program is complete, push it to your github repository
and compare it to the teacher's solution in S0065_rpg1_solution.py
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

class Character:

    def __init__(self, name, role, health, attackpower, healpower):
        self.name = name
        self.role = role
        self.max_health = health
        self._current_health = self.max_health
        self.attackpower = attackpower
        self.healpower = healpower


    def __repr__(self):
        return f" {self.name} {self.role} {self.max_health} {self._current_health} {self.attackpower} {self.healpower}"


    def melee(self, other):
        other._current_health -= self.attackpower
        print(self.name,"Used melee on", other.name,"!")


    # def get_hit(self, attackpower, other):
    #     self._current_health -= other.attackpower




    def heal(self, other):
        if(self.role == "Healer"):
            other._current_health += self.healpower
            print(self.name, "Used Heal on", other.name,"!")
        else:
            print(self.name,"Cannot heal!")


def printCharacters():
    print(character1)
    print(character2)


character1 = Character("Torben", "Tank", 100, 20, 10)
character2 = Character("Rasmus", "Healer", 100, 5, 30)
printCharacters()
character1.melee(character2)
printCharacters()
character2.heal(character1)
printCharacters()
character1.heal(character2)
printCharacters()
character2.melee(character1)