from methods import *

urunEkle("iphone 20", 90000)
urunEkle("samsung s20", 90000)

for i in urunleriGetir():
    print(i["urunAdi"])

urunGuncelle(1, "iphone 15 pro", 80000)

for i in urunleriGetir():
    print(i["urunAdi"])

