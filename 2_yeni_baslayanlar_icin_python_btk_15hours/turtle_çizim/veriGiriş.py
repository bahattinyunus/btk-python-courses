from turtle import*
N=int(numinput("poligon","kenar sayısı",5)) #  poligon pencerenin başlığı , kenar sayısı inputun başlığı , 5 önseçili olan değer
renk=textinput("renk","iç rengi")

pensize(4)

begin_fill()
fillcolor(renk)
circle(100,360,N)
end_fill()


circle(100,360,N)
