print("This program simualates a dice roll, the winner is the one who rolled \nthe highest number between you and a computer.")

import random
num1 = random.randint(1,6)
num2 = random.randint(1,6)

def rolldice():
    print("You rolled a",num1)
    print("Computer rolled a",num2)

rolldice()

if num1 > num2:
    print("The winner is you!!")

if not num1 >= num2:
    print("The winner is computer!!")

if num1 == num2:
    print("It's a tie!!")
