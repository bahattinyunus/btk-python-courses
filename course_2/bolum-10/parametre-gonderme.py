def selamlama(isim):
    return "Merhaba, " + isim

# print(selamlama("Sadık"))
# print(selamlama("Mehmet"))

def toplam(sayi1, sayi2):
    return sayi1 + sayi2

# print(toplam(10,20))
# print(toplam(10,30))

def yasHesapla(dogumYili):
    return 2024 - dogumYili

def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)

    kalanSure = 65 - yas

    if kalanSure > 0:
        return f"{isim}, emekliliğinize {kalanSure} yıl kaldı"
    else:
        return f"{isim}, zaten {abs(kalanSure)} yıl önce emekli oldunuz."

print(emekliligeKacYilKaldi(1983, "Sadık"))
print(emekliligeKacYilKaldi(1980, "Ali"))
print(emekliligeKacYilKaldi(1950, "Ayşe"))