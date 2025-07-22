from turtle import *
pensize(10)
shape('blank')

fillcolor('grey')
begin_fill()
for x in range (2):
    forward(100)
    right(90)
    forward(250)
    right(90)
end_fill()
     
pencolor('red')

penup()
goto(50,-80)
pendown()
fillcolor('red')
begin_fill()
circle(30)
end_fill()

penup()
goto(50,-155)
pendown()
pencolor('yellow')
fillcolor('yellow')
begin_fill()
circle(30)
end_fill()

penup()
goto(50,-235)
pendown()
pencolor('green')
fillcolor('green')
begin_fill()
circle(30)
end_fill()  

done()