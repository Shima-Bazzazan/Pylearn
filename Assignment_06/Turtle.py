import turtle
import math

turtle.bgcolor("black")
colors = ["red","purple","blue","green","yellow","orange"]

pen = turtle.Pen()
pen.shape("turtle")

index = 0
jump = 20
length = 0
pre_intern = 0

for i in range(3, 13):

    if index >= len(colors):
        index = 0
        pen.color(colors[index])
    else:
        pen.color(colors[index])

    pen.penup()
    pen.goto(jump, 0)
    pen.pendown()

    in_angle = ((i - 2) * 180) / i                       
    rotate = 180 - ((in_angle / 2) + (pre_intern / 2))
    length = 2 * jump * math.sin(math.radians(180/i))

    for j in range (i):
        pen.left(rotate)
        pen.forward(length)
        rotate = 180 - in_angle    

    index += 1 
    jump += 20
    pre_intern = in_angle

turtle.done()