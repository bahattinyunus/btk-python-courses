"""
    module1 (db)      : urunler
    module2 (methods) : urunEkle(), urunGuncelle(), urunleriGetir()
    module3 (app)     :

        yeni ürün ekleme => urunEkle("iphone 15", 60000)
        ürün güncelle    => urunGuncelle(1, "iphone 15 pro", 80000)
        ürünleri listele => urunleriGetir() 
"""

from methods import *

urunEkle("iphone 20", 90000)
urunEkle("samsung s20", 90000)

for i in urunleriGetir():
    print(i["urunAdi"])

urunGuncelle(1, "iphone 15 pro", 80000)

for i in urunleriGetir():
    print(i["urunAdi"])

