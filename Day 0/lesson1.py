from turtle import*

#We want to paint a house with windows.

#step 1: draw a square
shape("turtle")
speed(20)
width(5)

color("grey")

forward(210)
left(90)

forward(210)
left(90)

forward(210)
left(90)

forward(210)
left(90)

#end of square

#drawing a door

forward(70)
color("red")
begin_fill()
left(90)

forward(100)
right(90)

forward(70)
right(90)

forward(100)
end_fill()
penup()
goto(210, 210)
pendown()

color("brown")
begin_fill()
right(150)
forward(210)

left(120)
forward(210)
end_fill()

#end of door

#drawing the windows

penup()
goto(15, 130)
pendown()
color("black")
begin_fill()
right(150)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()

penup()
goto(195, 130)
pendown()
begin_fill()

right(90)
forward(60)

left(90)
forward(60)

left(90)
forward(60)

left(90)
forward(60)
end_fill()
penup()

#end of windows

exitonclick()