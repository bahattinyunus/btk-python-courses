urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (find, index)

for urun in urunler:
    index = urun.find('iphone')   # find bulursa 0 bulamazsa -1 döndürür
    if index > -1:    
        print(urun)


