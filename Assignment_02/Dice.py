
import random

print("-Dice-")

while True:

    user_choice= input("Please enter the roll/exit:")

    if user_choice=="exit":
        break

    elif user_choice=="roll":
       dice=random.randint(1,6)
       if dice==1:
           print("your chance is:",1)
        
       elif dice==2:
            print("your chance is:",2)
        
       elif dice==3:
            print("your chance is:",3)
        
       elif dice==4:
            print("your chance is:",4)
        
       elif dice==5:
            print("your chance is:",5)

       elif dice==6:
            print("your chance is:",6)
            print("You won:) Your reward is to roll the dice again!")
            user_choice=input()
            dice=random.randint(1,6)
            print("your reward is:",dice)

    else:
        print("wrong answer!")
   