"""
exercise: Object oriented role playing game, part 2 :

As always, read the whole exercise description carefully before you begin to solve the exercise.

Build on your solution of part 1.

Invent two new classes, which inherit from class Character. For example Hunter and Magician.
Your new classes shall have their own additional methods and/or attributes. Maybe they also override methods or attributes from class Character.

In the main program, let objects of your new classes fight against each other until one character is dead.
Print out what happens during the fight.

In each turn, a character uses one of its capabilities (methods). Then it's the other character's turn.
It is up to you, how your program decides in each turn, which capability to use.
For example, the decision may be based on randomness or on a clever strategy

Upgrade 1:
Each time a character uses one of it's capabilities, add some randomness to the used power.

Upgrade 2:
Let your characters fight against each other 100 times.
Keep track of the results.
Try to balance your character's capabilities in such a way that each character wins about half of the fights.

If you get stuck, ask google, the other pupils or the teacher (in this order).

When your program is complete, push it to your github repository.
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

    def dead(self, character):

        return self._current_health <= 0


    def heal(self, other):
        if(self.role == "Healer"):
            other._current_health += self.healpower
            print(self.name, "Used Heal on", other.name,"!")
        else:
            print(self.name,"Cannot heal!")


def printCharacters():
    print(character1)
    print(character2)



character1 = Character("Torben", "Tank", 100, 20, 0) #  name, role, max_healt, attackpower, healpower
character2 = Character("Rasmus", "Healer", 100, 5, 30)
# printCharacters()
# character1.melee(character2)
# printCharacters()
# character2.heal(character1)
# printCharacters()
# character1.heal(character2)
# printCharacters()
# character2.melee(character1)
turn = 0

while not dead() and turn < 100:
    turn += 1

printCharacters()