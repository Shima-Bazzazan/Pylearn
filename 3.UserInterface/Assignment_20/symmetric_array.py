
import math

def symmetric_array(user_array):
    array = []
    array = user_array.split(" ")
    last_array_member = len(array)-1
    if len(array) % 2 == 0 :
        for i in range(int(len(array)/2)):
            if array[i] == array[last_array_member - i]: 
                flag = 1
            else : 
                flag = 0
                break
    elif len(array) % 2 == 1:
        for i in range(len(array)-1):
            if i <= math.ceil(len(array)/2) :            
                if array[i] == array[last_array_member - i] :
                    flag = 1 
                else: 
                    flag = 0
                    break     
    if flag == 1:
        print("\nYour array is symmetric\n")          
    else:
        print("\nYour array is not symmetric\n")


user_array = input("Please enter your array(separate them with space): ")
symmetric_array (user_array)