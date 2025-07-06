liste = ["1","3","5","20b","abc","10a","60"]

# Liste elemanları içindeki sayısal değerleri bulma

# for x in liste:
#     try:
#         sonuc = int(x)
#         print(sonuc)
#     except ValueError:   #eğer sayıya dönüştüremezse atlar 
#         continue


# while True:
#     sayi = input("sayı: ")
#     if (sayi == "q"):
#         break
    
#     try:
#         sonuc = float(sayi)
#         print(f"girilen sayı: {sonuc}")
#         break
#     except ValueError:
#         print("geçersiz sayı")
#         continue


# 3: Dictionary ve key bilgilerini parametre olarak alan get(dict, key) fonksiyonu hazırlayınız.

urun = {"urunAdi":"samsung s20","fiyat":10000}

def get(liste, key):
    try:
        return liste[key]
    except KeyError:
        return None
    

sonuc = get(urun, "fiyat")
sonuc = get(urun, "urunAdi")

print(sonuc)
