import turtle
import time
import random

Liste = []
skor = 0
maxSkor = 0

# Ekran ayarları
w = turtle.Screen()
w.title("Yılan Oyunu")
w.setup(600, 600)
w.bgcolor("blue")
w.tracer(0)

# Yılan kafası
yn = turtle.Turtle()
yn.speed(0)
yn.shape("circle")
yn.color("red")
yn.penup()
yn.goto(0, 0)
yn.yon = "dur"

# Yem
yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("brown")
yem.penup()
yem.goto(0, 100)

# Hareket
def hareket():
    x = yn.xcor()
    y = yn.ycor()
    if yn.yon == "ust":
        yn.sety(y + 20)
    if yn.yon == "alt":
        yn.sety(y - 20)
    if yn.yon == "sag":
        yn.setx(x + 20)
    if yn.yon == "sol":
        yn.setx(x - 20)

# Yönler
def yukarigit():
    if yn.yon != "alt":
        yn.yon = "ust"
def asagigit():
    if yn.yon != "ust":
        yn.yon = "alt"
def sagagit():
    if yn.yon != "sol":
        yn.yon = "sag"
def solagit():
    if yn.yon != "sag":
        yn.yon = "sol"

w.listen()
w.onkeypress(yukarigit, "Up")
w.onkeypress(asagigit, "Down")
w.onkeypress(sagagit, "Right")
w.onkeypress(solagit, "Left")

# Yem yeme ve kuyruk ekleme
def ye():
    global skor, maxSkor
    if yn.distance(yem) < 20:
        # Yem yeni yere
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        yem.goto(x, y)

        # Kuyruk ekle
        kuyruk = turtle.Turtle()
        kuyruk.speed(0)
        kuyruk.shape("circle")
        kuyruk.color("white")
        kuyruk.penup()
        Liste.append(kuyruk)

        # Skor güncelle
        skor += 5
        if skor > maxSkor:
            maxSkor = skor
        w.title("Skor: {}  En Yüksek Skor: {}".format(skor, maxSkor))

    # Kuyruğu takip ettir
    uzunluk = len(Liste)
    for i in range(uzunluk - 1, 0, -1):
        x = Liste[i - 1].xcor()
        y = Liste[i - 1].ycor()
        Liste[i].goto(x, y)
    if uzunluk > 0:
        x = yn.xcor()
        y = yn.ycor()
        Liste[0].goto(x, y)

# Oyunu başa al
def baslangic():
    global skor
    time.sleep(0.5)
    yn.goto(0, 0)
    yn.yon = "dur"
    for parca in Liste:
        parca.goto(1000, 1000)
    Liste.clear()
    skor = 0
    w.title("Skor: {}  En Yüksek Skor: {}".format(skor, maxSkor))

# Ana döngü
while True:
    w.update()
    hareket()
    ye()

    # Kenara çarpma
    if yn.xcor() > 290 or yn.xcor() < -290 or yn.ycor() > 290 or yn.ycor() < -290:
        baslangic()

    # Kendine çarpma
    for parca in Liste:
        if parca.distance(yn) < 20:
            baslangic()

    time.sleep(0.1)
