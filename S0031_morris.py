"""
Exercise "Morris The Miner":

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Initial situation:
Morris has the attributes sleepiness, thirst, hunger, whisky, gold.
All attributes have the starting value 0.

Rules:
If sleepiness, thirst or hunger goes above 100, Morris the miner dies.
Morris can’t store more than 10 bottles of whisky.
No attribute may go below 0.

Possible moves for a turn:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Your task:
Write a program that gets Morris as much gold as possible in at most 1000 turns.

If you get stuck, ask google, the other pupils or the teacher (in this order).

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""


def sleep():
    status["sleepiness"] -= 10  # update sleepiness
    status["thirst"] += 1  # update thirst
    status["hunger"] += 1  # update hunger
    # check for values out of boundaries
    status["whisky"] += 0
    status["gold"] += 0

def mine():       #mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
    status["sleepiness"] += 5
    status["thirst"] += 5
    status["hunger"] += 5
    status["whisky"] += 0
    status["gold"] += 5

def eat():     # eat:     sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
    status["hunger"] -= 20
    status["thirst"] -= 5
    status["hunger"] -= 20
    status["whisky"] += 0
    status["gold"] -= 2

def buy_whisky(): #buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
    status["sleepiness"] += 5
    status["thirst"] += 1
    status["hunger"] += 1
    status["whisky"] += 1
    status["gold"] -= 1

def drink():    #drink:     sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0
    status["sleepiness"] += 5
    status["thirst"] -= 15
    status["hunger"] -= 1
    status["whisky"] -= 1
    status["gold"] += 0


def dead():
    return status["sleepiness"] > 100 or status["thirst"] > 100 or status["hunger"] > 100

def tjek():
    if status["sleepiness"] < 0:
        print("too much sleep")
        status["sleepiness"] = 0
    if status["thirst"] < 0:
        print("too much thirst")
        status["thirst"] = 0
    if status["hunger"] < 0:
        print("to much hunger")
        status["hunger"] = 0
    if status["whisky"] > 10:
        print("too much whisky")
        status["whisky"] = 10

status = {"turn": 0, "sleepiness": 0, "thirst": 0, "hunger": 0, "whisky": 0, "gold": 0}  # dictionary

while not dead() and status["turn"] < 1000:
    status["turn"] += 1
    activity = "nothing"

    if status["sleepiness"] >= 90:
        sleep()
        activity = "sleep()"
    elif status["hunger"] >= 80:
        eat()
        activity = "eat()"
    elif status["thirst"] >= 85 and not status["whisky"] >=1 :
        buy_whisky()
        activity = "buy_whisky()"

    elif status["thirst"] >= 85 and status["whisky"] >= 1:
        drink()
        activity = "drink()"
    else:
        mine()
        activity = "mine()"
    tjek()
    print(status, activity)
