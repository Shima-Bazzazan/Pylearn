
print("-Convert Seconds to Hours-")

while True:
    
    second=int(input("Please enter the seconds:"))
     
    if second<0:
        print("wrong time!")
    
    else:
        hour= (second // 3600)
        minute= (second % 3600) // 60
        second= second % 60
        print("your time is:", hour,":",minute,":",second)

    user_choice=input("Do you want to continue? Y/N \n")
    
    if user_choice=="N" or user_choice=="n":
        break 
    elif user_choice!="N" and user_choice!="n" and user_choice!="Y" and user_choice!="y":
        print("😐 😑 🤐")
        break