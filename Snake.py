
n=int (input("Please enter the length of the snake: "))

for i in range(n):
    if i % 2 == 0:
        print("*", end = "")
    else:
        print("#", end = "")