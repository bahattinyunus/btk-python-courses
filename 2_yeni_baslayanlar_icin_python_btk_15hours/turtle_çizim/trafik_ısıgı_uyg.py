from turtle import *
import time
w=Screen()
w.setup(300,700)
w.title("trafik isik uygulaması")

penup()
goto(0,180)
pendown()
pensize(4)

for i in range(2):
    forward(80)
    right(90)
    forward(220)
    right(90)
    
def kirmizi():
    penup()
    goto(40,140)
    pendown()
    fillcolor("red")
    shape("circle")
    shapesize(3)

def sari():
    penup()
    goto(40,70)
    pendown()
    fillcolor("yellow")
    shape("circle")
    shapesize(3)

def yesil():
    penup()
    goto(40,0)
    fillcolor("green")
    shape("circle")
    shapesize(3)
    
    
while True:    
    yesil()
    time.sleep(9)
    sari()
    time.sleep(3)
    kirmizi()
    time.sleep(9)

w.mainloop()

