print("Please enter the sides of the triangle:")
print("(The size of the sides must be greater than zero)")

a=float(input("1."))
b=float(input("2."))
c=float(input("3."))

if a<=0 or b<=0 or c<=0:
    print("There is no such triangle")
elif a<b+c and b<a+c and c<b+a:
    print("We have a triangle :)")
else:
    print("There is no such triangle")