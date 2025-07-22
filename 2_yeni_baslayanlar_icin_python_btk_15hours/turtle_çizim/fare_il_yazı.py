from turtle import *
pensize(3)
win=Screen()
win.setup(700,700)
penup()
def Nokta (x,y):
    goto(x,y)
    pendown()
win.onclick(Nokta) #tıklama olduğunda nokta fonksiyonunu çalıştırır
mainloop()




    