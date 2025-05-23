
markalar = ["Toyota","Bmw","Renault","Mercedes"]

sonuc = "Togg" not in markalar

sonuc = markalar + ["Ford","Citroen"]
print(sonuc)


ogrenci1 = ["Yiğit","Bilgi",2010,[70,80,90]]
ogrenci2 = ["Ada","Bilgi",2012,[70,70,80]]
ogrenci3 = ["Çınar","Turan",2017,[60,60,90]]

ogrenciler = [ogrenci1,ogrenci2,ogrenci3]


yasYigit = 2024 - ogrenciler[0][2]
yasAda = 2024 - ogrenciler[1][2]
yasCinar = 2024 - ogrenciler[2][2]

print(yasYigit, yasAda, yasCinar)


notYigit = (ogrenciler[0][3][0] + ogrenciler[0][3][1] + ogrenciler[0][3][2]) / 3
notAda = (ogrenciler[1][3][0] + ogrenciler[1][3][1] + ogrenciler[1][3][2]) / 3
notCinar = (ogrenciler[2][3][0] + ogrenciler[2][3][1] + ogrenciler[2][3][2]) / 3

print(notYigit, notAda, notCinar)
