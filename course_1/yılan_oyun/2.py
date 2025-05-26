import turtle
import time
import random

# Sabitler
DELAY_INITIAL = 0.1
DELAY_DECREMENT = 0.001
MOVE_INCREMENT = 20
BORDER = 330
FOOD_BORDER = 310
OUT_OF_SCREEN = 2000

# Skorlar
score = 0
high_score = 0

# Ekran kurulumu
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor('white')  # Arka plan rengi beyaz yapıldı
screen.setup(width=700, height=700)
screen.tracer(0)

# Yılan kafası
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")  # Yılan rengi yeşil yapıldı
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Yılan yemi
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Skor tablosu
score_display = turtle.Turtle()
score_display.speed(0)
score_display.shape("square")
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 310)
score_display.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))


# Fonksiyonlar
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + MOVE_INCREMENT)
    elif head.direction == "down":
        head.sety(head.ycor() - MOVE_INCREMENT)
    elif head.direction == "right":
        head.setx(head.xcor() + MOVE_INCREMENT)
    elif head.direction == "left":
        head.setx(head.xcor() - MOVE_INCREMENT)

# Klavye bağlamaları
screen.listen()
keys = {
    "w": go_up,
    "s": go_down,
    "d": go_right,
    "a": go_left,
    "Up": go_up,
    "Down": go_down,
    "Right": go_right,
    "Left": go_left,
}
for key, action in keys.items():
    screen.onkeypress(action, key)

# Ana döngü
delay = DELAY_INITIAL
while True:
    screen.update()

    # Sınır bölgesiyle çarpışma kontrolü
    if head.ycor() < -BORDER or head.ycor() > BORDER or head.xcor() < -BORDER or head.xcor() > BORDER:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Vücudun bölümlerini gizleme
        for segment in segments:
            segment.goto(OUT_OF_SCREEN, OUT_OF_SCREEN)
        # Bölümleri temizle
        segments.clear()

        # Skoru ve gecikmeyi sıfırla
        score = 0
        delay = DELAY_INITIAL

        score_display.clear()
        score_display.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Yiyecekle çarpışma kontrolü
    if head.distance(food) < 20:
        # Yemeği rastgele bir yere taşıma
        x = random.randint(-FOOD_BORDER, FOOD_BORDER)
        y = random.randint(-FOOD_BORDER, FOOD_BORDER)
        food.goto(x, y)

        # Başa yeni bölüm ekleme
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")  # Yeni segment rengi de yeşil yapıldı
        new_segment.penup()
        segments.append(new_segment)

        # Gecikmeyi kısalt ve skoru arttır
        delay -= DELAY_DECREMENT
        score += 10

        if score > high_score:
            high_score = score
        score_display.clear()
        score_display.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Segmentleri ters sırada hareket ettir
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # 0. bölümü başa taşı
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Gövdeyle çarpışma olup olmadığını kontrol edin
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Segmentleri gizle
            for seg in segments:
                seg.goto(OUT_OF_SCREEN, OUT_OF_SCREEN)
            segments.clear()
            score = 0
            delay = DELAY_INITIAL

            # Skoru güncelle
            score_display.clear()
            score_display.write(f"Score: {score} High Score: {high_score}", align="center",
                                font=("Courier", 24, "normal"))

    time.sleep(delay)

screen.mainloop()