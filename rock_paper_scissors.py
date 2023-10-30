import random

print("-rock_paper_scissors")

computer_score=0
user_score=0

while True:
    
    computer_number= random.randint(1,3)
    
    if computer_number==1:
        computer_choice="rock"

    elif computer_number==2:
        computer_choice="scissors"

    elif computer_number==3:
        computer_choice="paper"

    user_choice= input("Please enter your choice: paper/scissors/rock/exit \n")

    if user_choice=="exit":
        break

    print("💻:", computer_choice)
    print("👩/🧑:", user_choice)


    if user_choice=="rock" and computer_choice=="paper":
        computer_score+=1

    elif user_choice=="rock"and computer_choice=="scissors":
        user_score+=1

    elif user_choice=="scissors"and computer_choice=="paper":
        user_score+=1

    elif user_choice=="scissors"and computer_choice=="rock":
        computer_score+=1

    elif user_choice=="paper"and computer_choice=="scissors":
        computer_score+=1

    elif user_choice=="paper"and computer_choice=="rock":
        user_score+=1

    print("the score of 💻 :", computer_score)
    print("the score of 👩/🧑:", user_score)