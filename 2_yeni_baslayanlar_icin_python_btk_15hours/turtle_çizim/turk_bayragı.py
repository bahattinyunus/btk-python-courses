from turtle import *
title("turk bayragı")
setup(width=600,height=400)
bgcolor("red")

def renkKonum(renk,x,y):
    penup()
    goto(x,y)
    pendown()
    color(renk)
    begin_fill()

def yildiz():
    renkKonum("white",80,25)
    for i in range(5):
        forward(50)
        right(144)
        forward(50)
        right(-72)

    end_fill()    
         
def hilal(cap):
    circle(cap)
    end_fill()
    
    
renkKonum("white",-110,-120)
hilal(130)
renkKonum("red",-70,-90)
hilal(100)

yildiz()
mainloop()

             