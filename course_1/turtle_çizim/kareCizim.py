from turtle import *
def kareCizim(mesafe): #kare çizim fonksiyonu
    for a in range (1,5):
        forward(mesafe)
        left(90)
        
hideturtle()
pensize(2)

# kareCizim(50)
# kareCizim(100)
# kareCizim(150)

hideturtle()
    
pensize(2)
x=int(input("kare sayisi gir:"))
x+=1     
for a in range(x):
    kareCizim(50*a)