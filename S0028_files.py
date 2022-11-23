"""
Exercise "Reading from a file":

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

create a text file with a editor of your choice (pycharm, notepad, notepad++, etc.)
each row shall consist of a person's name, followed by a space and a number, representing the person's age.
save the file in a subdirectory "data" of your solution directory

write a program which reads the file into a list of strings
then use the content of each string to print out a row like:
    <name> is <age> years old.

if you get stuck, ask google, the other pupils or the teacher (in this order).

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

# line_number = 0
# files = open("data/files.txt") as file:
#     for line in file:
#         line_number += 1
#         print(f"line {line_number}: {line.strip()}")

line_number = 0
my_file = open("data/files.txt", "r")
for line in my_file:
     data = my_file.read()

     # data_name = data.replace(' ', '\n')
     stringlist = data.split(' ')

     print(stringlist)

my_file.close()


