
n= int(input("Please enter the length of list: "))

list = [] 
temp_list = []  

print("Please enter the members of the list: ")

while n>0:
    
    list.append(int(input()))
    n-=1

for member in list:
    if member not in temp_list:
        temp_list.append(member)

print("Non-repetitive List =", temp_list)