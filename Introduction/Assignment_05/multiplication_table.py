

def multiplication_table(num1: int,num2: int):
    for i in range (1,num1+1):
        for j in range(1,num2+1):
            print("{:6d}".format(j*i),end=" ")
        print()

n = int(input("Please enter num1: "))
m = int(input("Please enter num2: "))

multiplication_table(n, m)