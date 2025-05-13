from turtle import *

bgcolor("black")
speed(0)
width(10)

radius = 150

for i in range(15):
    color("black", "cyan")
    right(18)
    
    for j in range(10):
        begin_fill()
        circle(radius)
        end_fill()
            
        right(18)
        
    
    color("black", "black")
    right(18)
    
    for j in range(10):
        begin_fill()
        circle(radius-5)
        end_fill()
            
        right(18)
        
        
    radius = radius - 10

hideturtle()
done()