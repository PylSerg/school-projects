from turtle import *

speed(10)
width(3)

radius = 100

for i in range(5):
    color("red")
    right(18)

    for j in range(10):
        circle(radius)
        right(36)

        
    color("black")
    right(18)

    for j in range(10):
        circle(radius)
        right(36)
        
    radius = radius - 10

hideturtle()
done()