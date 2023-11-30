
print("-Fibonacci sequence-")

n=int(input("Enter the length of the Fibonacci sequence:"))

x1=0
x2=1
i=0

if n<=0:
    print("wrong number!")

elif n==1:
    print("Fibonacci sequence is:", x1)

else:
    print("Fibonacci sequence is:")
    while i<n:
        print(x1)
        temp=x1 + x2
        x1=x2
        x2=temp
        i+=1