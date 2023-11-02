
import random

friends=["Shima" , "Sajjad", "hasti" , "hami" , "Iman" , "shabnam" , "atefeh" , "Javid" , "morteza" , "reza" , "Farzane" ,"roya"]

good_chars=[]
bad_chars=[]
temp=0
user_mistakes=0

x= random.randint(0, len(friends)-1)
computer_choice=friends[x].lower()


while user_mistakes<6:
    
    for i in range (len(friends[x])):
        
        if computer_choice[i] in good_chars:
            print(computer_choice[i], end=" ")
            
        else:
            print ("-", end=" ")
    
    if temp==1:
        print("\n You win 🎉")
        break
            
    user_guess=input("Please write your guess: ")
        
    if user_guess.lower() in friends[x].lower():
        good_chars.append(user_guess)

    else:
        bad_chars.append(user_guess)
        user_mistakes+=1
    
    temp=1

    for i in range (len(friends[x])):
        if computer_choice[i] not in good_chars:
            temp=0
            break

if len(bad_chars)==6:
    print("You losse ☠")
