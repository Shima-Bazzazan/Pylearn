import qrcode

name = input("Please enter your Name: ")
last_name=input("Please enter your Lastname: ")
phone_number = input("Please enter your phone number: ")

img = qrcode.make(name+" "+last_name +"\n"+phone_number)
img.save("Shimdal_qrcode.png")