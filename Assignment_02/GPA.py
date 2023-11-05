
print ("-GPA-")

ave=0
sum=0
i=0

while True:
    
    score=input("Please enter your score/exit:")    
    
    if score=="exit":
        break
    
    sum= sum + float(score)
    i+=1
    ave=sum/i            

print("your GPA is:",ave)    
