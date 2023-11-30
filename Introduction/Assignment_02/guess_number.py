import random
print("-Guess number-")
computer_number=random.randint(0,50)
i=1

while True:
   
    user_number=int (input("Please enter your number: your number between (0,50) \n"))

    if user_number>computer_number:
        print("go down ⬇")
   
    elif user_number<computer_number:
        print("go up ⬆")
    
    elif user_number==computer_number:
        print("You won after",i ,"times 🎉")
        break
    i+=1