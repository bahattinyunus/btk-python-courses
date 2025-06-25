sayilar = [3,5,7,2,12,32,45]

# 1- "sayilar" listesindeki her bir elemanı yazdırınız.

# for sayi in sayilar:
#     print(sayi)

# 2- "sayilar" listesinde hangi sayılar 3' ün katıdır?

# for sayi in sayilar:
#     if sayi % 3 == 0:
#         print(sayi)

# 3- "sayilar" listesinde tüm sayıların toplamı nedir?

# toplam = 0
# for sayi in sayilar:
#     toplam += sayi
# print(toplam) 

urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (find, index)

# for urun in urunler:
#     index = urun.find('iphone')
#     if index > -1:
#         print(urun)

# 5- "urunler" listesinde kaç adet samsung ürünü vardır?
adet = 0
for urun in urunler:
    index = urun.find('samsung')
    if index > -1:
        adet += 1

print(adet)
        

