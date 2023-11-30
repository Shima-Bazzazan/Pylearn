print("-Convert Hours to Seconds-")


while True:
    
    sum=0

    hour=int(input("please enter the hour:"))
    minutes= int(input("please enter the minutes:"))
    second= int(input("please enter yoyr second:"))

    if second<0 or hour<0 or minutes<0:
        print("wrong time!")
    
    elif second>59 or hour>24 or minutes>59:
        print("wrong time!")

    else:
        print( hour,":",minutes,':',second)
        sum=hour*3600 + minutes*60 + second
        print("Your times is:",sum, "seconds")

    user_choice=input("Do you want to continue? Y/N \n")
    
    if user_choice=="N" or user_choice=="n":
        break
    elif user_choice!="N" and user_choice!="n" and user_choice!="Y" and user_choice!="y":
        print("😐 😑 🤐")
        break
    