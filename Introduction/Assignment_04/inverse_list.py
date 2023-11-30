

n= int(input("Please enter the length of list: "))

list = [] 
inverse_list = []  

print("Please enter the members of the list: ")

while n>0:
    
    list.append(int(input()))
    n-=1

print("List= ",list)

for member in range(len(list)-1, -1, -1):
    inverse_list.append(list[member])

print("Inverse List =",inverse_list)