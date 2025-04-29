from turtle import *

shape("turtle")
speed(5)

# Опускаємо черепашку вниз на радіус кола
up()
goto(x=0, y=-300)

down()
width(5)

# Малюємо жовтий круг
fillcolor("yellow")

begin_fill()
circle(300)
end_fill()

# Переміщуємо черепашку для малювання лівого ока
up()
goto(x=-100, y=50)

# Малюємо чорний круг
down()

fillcolor("black")

begin_fill()
circle(50)
end_fill()

# Переміщуємо черепашку для малювання правого ока
up()
goto(x=100, y=50)

# Малюємо чорний круг
down()

fillcolor("black")

begin_fill()
circle(50)
end_fill()

# Переміщуємо черепашку для малювання посмішки
up()
goto(x=-150, y=-130)

# Малюємо посмішку
down()

width(20)
right(60)
circle(180, 120)   # Малюємо дугу в 120° від кола з радіусом 180px

# Ховаємо черепашку та очікуємо завершення виконання програми
hideturtle()
done()