def selamlama(isim = "Kullanıcı", mesaj = "İyi Günler"):
    return f"{mesaj} {isim}"

sonuc = selamlama("Sadık","Merhaba")
sonuc = selamlama("Ali","Selam")
sonuc = selamlama("Ali")
sonuc = selamlama()

def usAlma(taban,us=2):
    return taban ** us

sonuc = usAlma(2,3)
sonuc = usAlma(5)

def toplam(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def islem(a,b,fn = toplam):
    return fn(a,b)

sonuc = islem(10,20,cikarma)    
sonuc = islem(10,20)    
sonuc = islem(10,20,toplam)    

print(sonuc)