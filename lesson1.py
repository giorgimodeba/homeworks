from turtle import *

#we wont to paint a hous

#step 1:   draw a square
speed(35)
width(10)
color("green")
begin_fill()
forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90)
end_fill()
#end of square

#drawing a door 

forward(125)
color("purple")
begin_fill()
left(90)
forward(120) #heigt of the door
right(90)
forward(50)
right(90)
forward(120)
end_fill()

penup()
goto(300, 300)
pendown()

color("red")
begin_fill()
right(150)
forward(300)
left(120)
forward(300)
end_fill()

penup()
goto(280, 300)
pendown()

right(330)
color("green")
forward(50)

color("blue")
begin_fill()
right(90)
forward(60)
left(90)
forward(100)
left(90)
forward(60)
left(90)
forward(100)
end_fill()

penup()
goto(130, 150)
pendown()

color("green")
left(90)
forward(60)

color("blue")
begin_fill()
right(90)
forward(100)
left(90)
forward(55)
left(90)
forward(100)
left(90)
forward(55)
end_fill()









exitonclick()






