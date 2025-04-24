from turtle import *

setup(1200, 800)
shape("turtle")
speed(5)

width(10)

up()
goto(-300, 0)

down()
color("red")
circle(100)

up()
goto(-150, 0)

down()
color("blue")
circle(100)

up()
goto(0, 0)

down()
color("green")
circle(100)

up()
goto(150, 0)

down()
color("yellow")
circle(100)

up()
goto(-225, -150)

down()
color("purple")
circle(100)

up()
goto(-75, -150)

down()
color("orange")
circle(100)

up()
goto(75, -150)

down()
color("pink")
circle(100)

up()
goto(300, 200)

down()
color("black", "tomato")

begin_fill()
forward(100)
left(120)
forward(100)
left(120)
forward(100)
end_fill()

done()