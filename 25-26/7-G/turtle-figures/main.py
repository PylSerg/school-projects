from turtle import *

# shape() — форма
shape("turtle")

# speed() — швидкість
speed(5)

# setup() — розмір екрану
setup(1200, 800)

# bgcolor() — колір фону
bgcolor("light blue")

# width() — товщина лінії
width(10)

# begin_fill() — почати зафарбовування
begin_fill()
# color(колір контуру, колір зафарбовування)
color("black", "blue")

# circle() — коло
circle(200)

# end_fill() — закінчити зафарбовування
end_fill()

# up() — підняти олівець
up()

# goto(x, y) — перейти до координат
goto(100, -100)

# down() — опустити олівець
down()

# begin_fill() — почати зафарбовування
begin_fill()

# color(колір контуру, колір зафарбовування)
color("black", "red")

# for i in range(8) — цикл, який повторюється 8 разів
for i in range(8):
    # forward(150) — рухатися вперед на 150 кроків
    forward(150)
    
    # left(45) — повернути ліворуч на 45 градусів
    left(45)

# end_fill() — закінчити зафарбовування
end_fill()

# hideturtle() — приховати черепашку
hideturtle()

# done() — закрити вікно
done()