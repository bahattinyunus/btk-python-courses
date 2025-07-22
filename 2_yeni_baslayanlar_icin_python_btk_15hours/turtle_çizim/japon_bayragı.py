from turtle import *
pensize(10)
shape('blank')
for x in range (2):
    forward(150)
    right(90)
    forward(100)
    right(90)
    
pencolor('red')

penup()
goto(75,-80)
pendown()
fillcolor('red')
begin_fill()
circle(30)
end_fill()
   