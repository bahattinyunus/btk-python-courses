import turtle,time,random 
Liste=[]
skor=0
maxSkor=0

#çerceve ayarları
w=turtle.Screen()
w.title("yılan oyunu")
w.setup(600,600)
w.bgcolor("blue")
w.tracer(0)

#yılan kafa
yn=turtle.Turtle()
yn.speed(0)
yn.shape("circle")
yn.color("red")
yn.penup()
yn.goto(0,0)
yn.yon="dur"


def hareket():
    if yn.yon=="ust":
        y=yn.ycor
        yn.sety(y+20)
    if yn.yon=="alt":
        y=yn.ycor
        yn.sety(y-20)
    if yn.yon=="sag":
        y=yn.ycor
        yn.sety(x+20) 
    if yn.yon=="sol":
        y=yn.ycor
        yn.sety(x-20)             

def yukarigit():
    if yn.yon!="alt":
        yn.yon="ust"
def asagigit():        
    if yn.yon!="ust":
        yn.yon="alt"    
def sagagit():    
    if yn.yon!="sol":
        yn.yon="sag"
def solagit():        
    if yn.yon!="sag":
        yn.yon="sol"

w.listen()
w.onkeypress(yukarigit,"up")
w.onkeypress(asagigit,"down")
w.onkeypress(sagagit,"right")
w.onkeypress(solagit,"left")
                        
while True:
    w.update()
    hareket()
    time.sleep(0.1) 
    
yem=turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("brown")
yem.penup()
yem.goto(0,100)



def ye():
    if yn.distance(yem)<20:
     x=random.randint(-280,280)
     y=random.randint(-280,280)
     yem.goto(x,y)
     
     kuyruk=turtle.Turtle()
     kuyruk.speed(0)
     kuyruk.shape("circle")
     kuyruk.color("white")
     kuyruk.penup()
     Liste.append(kuyruk)
    global skor,maxSkor
     skor+=5
     if skor>maxSkor:
         maxSkor=skor
         w.title("Skor:{}  en yüksek skor: {}".format(skor,maxSkor)) 
   uzunluk=len(Liste)
   for indis in range(uzunluk-1,0,-1):
       x=Liste[indis-1].xcor()
       y=Liste[indis-1].ycor()
       Liste[indis].goto(x,y)
    if len(Liste)>0:
        x=yn.xcor()
        y=yn.ycor()
        Liste[0].goto(x,y)

def baslangic():
    time.sleep(0.1)
    yn.goto(0,0)
    yn.yon="dur"
   
    for eklem in Liste:
        eklem.goto(1000,1000)
    Liste.clear()
    skor=0
    w.title("skor: {} en yüksek puan {}".format(skor,maxSkor))
    
while True:
    w.update()
    ye()
    hareket()
    if yn.xcor()>290 or yn.xcor()<-290 or yn.ycor()>290 or yn.ycor()<-290:
        baslangic()
    for eklem in Liste:
        if eklem.distance(yn)<20:
            baslangic()
    time.speed(0.1)
w.mainloop()
        
                                        
                                 