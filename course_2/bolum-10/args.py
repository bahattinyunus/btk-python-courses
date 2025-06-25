# sayilar = (10,20,30,40,50)

# def toplam(liste):
#     sonuc = 0
#     for i in liste:
#         sonuc += i
#     return sonuc

def toplam(*args):
    print(args)
    print(type(args))
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

# sonuc = toplam(10,20)
# sonuc = toplam(10,20,30)
sonuc = toplam(10,20,30,40)

print(sonuc)