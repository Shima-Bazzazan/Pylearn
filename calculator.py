import math

print("Welcomr to my calculator :)")
print("Please select a number:")
print("1. + : sum")
print("2. - : sub")
print("3. * : mul")
print("4. / : div")
print("5. √ : sqr")
print("6. ! : fact")
print("7. sin")
print("8. cos")
print("9. tan")
print("10. cot")
print("11. log")

choice=input()

if choice=="1" or choice=="2" or choice=="3" or choice=="4":
    
    num1=float(input("Please nter your first number: "))
    num2=float(input("Please enter your second number: "))

else:
    num=float(input("Please enter your number: "))

if choice=="1":
    result=num1 + num2

elif choice=="2":
    result= num1 - num2

elif choice=="3":
    result= num1 * num2

elif choice=="4":
    if num2==0:
        result="Cannot be calculated!"
    else:
        result= num1 / num2

elif choice=="5":
    if num<0:
        result="Cannot be calculated!"
    else:
        result= math.sqrt(num)

elif choice=="6":
    if num<0:
        result="Cannot be calculated!"
    else:
        result= math.factorial(int(num))

elif choice=="7":
    result= math.sin (math.radians (num)) 

elif choice=="8":
    result= math.cos (math.radians (num))

elif choice=="9":
    if math.cos (math.radians (num))==0:
        result="Cannot be calculated!"
    else:
        result= math.tan (math.radians (num))

elif choice=="10":
    if math.tan (math.radians (num))==0:
        result="Cannot be calculated!"
    else:
        result= 1 / (math.tan (math.radians (num)))

elif choice=="11":
    if num<=0:
        result="Cannot be calculated!"
    else:
        result=math.log(num)  


print (result)
