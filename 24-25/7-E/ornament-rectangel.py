from turtle import *

bgcolor("black")
speed(0)
width(10)

radius = 150

for i in range(15):
    color("cyan", "cyan")
    right(3)
    
    for j in range(20):
        begin_fill()
        for y in range(4):
            forward(radius*2)
            right(90)
        end_fill()
            
        right(18)
        
    
    color("black", "black")
    right(3)
    
    for j in range(20):
        begin_fill()
        for y in range(4):
            forward(radius*2)
            right(90)
        end_fill()
            
        right(18)
        
        
    radius = radius - 10

done()