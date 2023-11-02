
array=[]
temp=0
i=0

while(True):
    user_choice=int(input("please enter your array: "))
    array.append(user_choice)
    if temp<=user_choice:
        temp=user_choice

    else:
        i=1
    
    user_choice=input(" Dyou want continue? y/n ")
    if user_choice=="n":
        break
if i==0:
    print(array)
    print("the the array  is sorted")
else:
    print(array)
    print("the the array  is not sorted")
