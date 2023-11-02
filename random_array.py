
import random

n = int(input("Please enter the size og the array: "))
array= []

for i in range(n):
    while True:
        computer_choice = random.randint(0, 100)

        if computer_choice not in array:
            array.append(computer_choice)
            break
print (array)