print("Please enter your height and weight:")

weight=float(input("your weight (kg):"))
height=float(input("your height (m):"))

bmi= weight / (height ** 2)

if bmi<18.5:
    print("BMI=",bmi)
    print("your body mass index is Underweight")

elif 18.5<=bmi<25:
    print("BMI=",bmi)
    print("your body mass index is Normal Weight")
    

elif 25<=bmi<30:
    print("BMI=",bmi)
    print("your body mass index is Overweight")

elif 30<=bmi<35:
    print("BMI=",bmi)
    print("your body mass index is Obesity")

elif 35<=bmi<40:
    print("BMI=",bmi)
    print("your body mass index is Extreme Obesity")

else:
    print(":|")
    
