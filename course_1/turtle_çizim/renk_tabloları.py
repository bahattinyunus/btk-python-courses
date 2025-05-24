from turtle import *
colormode(255)
color(255,0,0)
pensize(6)
def ucgen():
    for x in range(3) :
        forward(200)
        left(120)
def kare():
    for x in range(4) :
      forward(200)
      right(90)
            
begin_fill()
fillcolor(165,42,42)
ucgen()
end_fill()

begin_fill()
fillcolor(128,128,128)
kare()
end_fill()
    
        