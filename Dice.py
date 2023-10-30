import random

print("-Dice-")

while True:

    user_choice= input("Please enter the roll/exit:")

    if user_choice=="exit":
        break

    elif user_choice=="roll":
        dice=random.randint(1,6)
        print("yor chance is:", dice)
        if dice==6:
                print("You won:) Your reward is to roll the dice again!")
                user_choice=input()
                dice=random.randint(1,6)
                print("your reward is:",dice)

    else:
        print("wrong answer!")
