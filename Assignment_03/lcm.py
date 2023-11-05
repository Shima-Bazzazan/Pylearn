
while (True):

    num1=int (input("please enter first number:"))
    num2=int (input("please enter second number:"))

    if num1>0 and num2>0:
        break
    else:
        print("Please enter another numbers")

gcd=0
if num1>num2:
   gcd=num2
else:
    gcd=num1
    
for i in range (gcd,0,-1):
        
    if num1 % i==0 and num2 % i==0:
        gcd=i
        break

lcm=int((num1 * num2) / gcd)
print("lcm is: ", lcm)