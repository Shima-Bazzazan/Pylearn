#GPA_Calculation

def gpa():

    print("Please enter your details")
    name=input("Name: ")
    lastname=input("Lastname: ")

    try:
        print("\nPlease enter your grades")
        print("Your score should be between (0,20)\n")

        grade1=float(input("First grade: "))
        grade2=float(input("Second grade: "))
        grade3=float(input("Third grade: "))

        if 0<=grade1<=20 and 0<=grade2<=20 and 0<=grade3<=20:
           
            gpa=(grade1 + grade2 + grade3) / 3 
            
            if gpa>=17:
                print("Dear", name, "your GPA is", gpa,".Your academic status is Great.")

            elif gpa<17 and gpa>=12:
                print("Dear", name, "your GPA is", gpa,".Your academic status is Normal.")

            elif 0<=gpa<12:
                print("Dear", name, "your GPA is", gpa,".Your academic status is Fail.")
           
        else:
            print("Your input out of range!")
    except:
        print("Inputs is not valid")
gpa()