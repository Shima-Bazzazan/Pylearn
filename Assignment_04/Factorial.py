
fact_number = int(input("Please enter a number: "))

fact=1
i=1
temp = 1

while (temp < fact_number):
    
    fact =fact * (i + 1)
    i+= 1
    temp = fact

if temp == fact_number:
    
    print("Yes")
else:
    
    print("No")