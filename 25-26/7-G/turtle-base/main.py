# Імпорт бібліотеки turtle
from turtle import *

# Очистка екрану
reset()

# Створення черепашки
shape("turtle")

# Підняття черепашки
up()
# Переміщення черепашки
goto(300, 100)

# Встановлення товщини лінії
width(10)
# Встановлення кольору лінії
color("red")

# Опускання черепашки
down()
# Переміщення черепашки
forward(200)
# Поворот черепашки
left(90)

forward(200)
left(90)
forward(200)
left(90)
forward(200)

up()
color("black")
goto(-300, -100)

width(5)
color("blue")

down()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

# Завершення програми
exitonclick()