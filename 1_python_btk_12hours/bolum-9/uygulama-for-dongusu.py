urunler = [
    {"urunAdi":"Hp Victus 1", "fiyat": 32999},
    {"urunAdi":"Lenovo ThinkPad", "fiyat": 25499},
    {"urunAdi":"Apple Macbook", "fiyat": 49999},
    {"urunAdi":"Huawei Matebook", "fiyat": 26999},
    {"urunAdi":"Casper Nirvana", "fiyat": 20000},
    {"urunAdi":"Hp Victus 2", "fiyat": 30000},
]



# for urun in urunler:
    # print(f"{urun['urunAdi']} marka ürünün fiyatı {urun['fiyat']} Türk Lirası.")



# toplam = 0
# for urun in urunler:
#     toplam += urun["fiyat"]
# print(f"ürün toplamı: {toplam}")



# for urun in urunler:
#     if (urun["fiyat"] >= 25000 and urun["fiyat"] <= 40000):
#         print(f"{urun["urunAdi"]}")



kelime = input("aramak istediğiniz ürün: ")

for urun in urunler:
    if(urun["urunAdi"].lower().find(kelime.lower()) > -1):
        print(f"{urun['urunAdi']}")
        
        
        
        
# urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

# # 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (find, index)

# for urun in urunler:
#     index = urun.find('iphone')   # find bulursa 0 bulamazsa -1 döndürür
#     if index > -1:    
#         print(urun)


        