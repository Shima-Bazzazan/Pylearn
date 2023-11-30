#Make_Triangle

def triangle():
    
    try:
        print("Please enter the sides of the triangle:")
        print("(The size of the sides must be greater than zero)\n")
        
        num1 = float(input("The length of first side: "))
        num2 = float(input("The length of second side: "))
        num3 = float(input("The length of third side: "))

        if (num1 + num2 > num3 and num2 + num3 > num1 and num3 + num1 > num2):
            print("We have a triangle :)")

        else:
            print("There is no such triangle!")
            
    except:
             print("Inputs is not valid")

triangle()