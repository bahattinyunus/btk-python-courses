import random   
sayi=random.randint(1,12)
tahmin=int(input("tahmin et...:"))
skor=5
while True:
    if sayi==tahmin:
        print("kazandınız..  skorunuz..: ",skor)
        break
    else:
        print("olmadı..   skorun....: ",skor)
        skor-=1
        tahmin=int(input("tahmin et....:"))

