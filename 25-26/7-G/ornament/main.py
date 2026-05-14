from turtle import *

radius = 200

shape("turtle")
speed(0)

width(3)

for i in range(10):
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

    radius = radius - 5

done()