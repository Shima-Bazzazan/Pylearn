print("Please enter your details:")
name=input("Name: ")
lastname=input("Lastname: ")

print("Please enter your grades:")

grade1=float(input("first grade: "))
grade2=float(input("second grade: "))
grade3=float(input("third grade: "))

ave=(grade1 + grade2 + grade3) / 3

if ave>=17:
    print("Dear", name, "your GPA is", ave,".Your academic status is Great.")

elif ave<17 and ave>=12:
    print("Dear", name, "your GPA is", ave,".Your academic status is Normal.")

else:
    print("Dear", name, "your GPA is", ave,".Your academic status is Fail.")
