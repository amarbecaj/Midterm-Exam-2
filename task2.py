"""
===================   TASK 2   ====================
* Name: Roll The Dice
*
* Write a script that will simulate rolling the
* dice. The script should fetch the number of times
* the dice should be "rolled" as user input.
* At the end, the script should print how many times
* each number appeared (1 - 6).
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

from random import randint

import random

one=0
two=0
three=0
four=0
five=0
six=0

for i in range(100):
    rolled=random.randint(1,6)

    if rolled==1:
        one+=1
    elif rolled==2:
        two +=1
    elif rolled==3:
        three +=1
    elif rolled==4:
        four +=1
    elif rolled==5:
        five +=1
    elif rolled==6:
        six +=1


print("Rolled on One: " + str(one))
print("Rolled on Two: " + str(two))
print("Rolled on Three: " + str(three))
print("Rolled on Four: " + str(four))
print("Rolled on Five: " + str(five))
print("Rolled on Six: " + str(six))