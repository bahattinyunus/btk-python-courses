# Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yaz 
def yazdir(text, adet):
    return text * adet

# print(yazdir("Merhaba ", 5))



def yaziTura():
    import random
    sayi = random.random()

    if sayi > 0.5:
        return "Tura"
    else:
        return "Yazı"
    
sonuc = yaziTura()



def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if(sayi > 1):
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

asalSayilariBul(10,30)



def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if(sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenleriBul(20))

