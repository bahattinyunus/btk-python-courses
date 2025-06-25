def toplam():
    return 10+20

sonuc = toplam()

def yil():
    import datetime
    return datetime.datetime.now().year

def saat():
    import datetime
    return datetime.datetime.now().hour

def yasHesapla():
    return yil() - 1983

print(yasHesapla())

def selamlama():
    if(saat() < 12):
        return "Günaydın"
    else:
        return "Merhaba"
    
print(selamlama())